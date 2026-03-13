#!/usr/bin/env python3
"""
LAPTIME PREDICTOR - Terminal Interface
A beautiful racing lap time predictor with ASCII art and rich terminal UI.
"""

import sys
import time
import os

try:
    from rich.console import Console
    from rich.table import Table
    from rich.panel import Panel
    from rich.text import Text
    from rich.columns import Columns
    from rich.align import Align
    from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
    from rich import box
    from rich.style import Style
    from rich.rule import Rule
    import pyfiglet
except ImportError:
    print("Installing required packages...")
    os.system("pip install rich pyfiglet --break-system-packages -q")
    from rich.console import Console
    from rich.table import Table
    from rich.panel import Panel
    from rich.text import Text
    from rich.columns import Columns
    from rich.align import Align
    from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
    from rich import box
    from rich.style import Style
    from rich.rule import Rule
    import pyfiglet

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from model.data import TRACKS, CARS, CATEGORY_LABELS, ASCII_MAPS
from model.predictor import predict_lap_time

console = Console()

# ─── Color Theme ────────────────────────────────────────────────────────────
THEME = {
    "primary":   "bold white",
    "accent":    "bold yellow",
    "dim":       "dim white",
    "green":     "bold green",
    "red":       "bold red",
    "blue":      "bold cyan",
    "header":    "bold white on red",
    "category":  "bold yellow",
    "track":     "bold cyan",
    "car":       "bold white",
    "result":    "bold green",
}

CATEGORY_COLORS = {
    "f1":    "bold red",
    "gt3":   "bold cyan",
    "gt4":   "bold blue",
    "rally": "bold yellow",
}


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def print_banner():
    """Print the main ASCII art banner"""
    clear()
    fig = pyfiglet.figlet_format("LAPTIME", font="big")
    fig2 = pyfiglet.figlet_format("PREDICTOR", font="big")

    banner_text = Text()
    for line in fig.split("\n"):
        banner_text.append(line + "\n", style="bold red")
    for line in fig2.split("\n"):
        banner_text.append(line + "\n", style="bold white")

    console.print(Panel(
        Align.center(banner_text),
        border_style="red",
        padding=(0, 2),
    ))

    console.print(Align.center(
        Text("🏁  Racing Lap Time Predictor  v1.0  🏁", style="bold yellow")
    ))
    console.print()


def print_section_header(title: str, subtitle: str = ""):
    """Print a styled section header"""
    console.print()
    console.print(Rule(style="red dim"))
    console.print(f"  [bold red]▸[/bold red]  [bold white]{title}[/bold white]", end="")
    if subtitle:
        console.print(f"  [dim]{subtitle}[/dim]", end="")
    console.print()
    console.print(Rule(style="red dim"))
    console.print()


def get_ascii_map(track_id: str, track_name: str) -> str:
    """Get ASCII map for a track, fallback to default"""
    # Try exact match first, then partial match
    if track_id in ASCII_MAPS:
        return ASCII_MAPS[track_id]
    for key in ASCII_MAPS:
        if key in track_id or track_id in key:
            return ASCII_MAPS[key]
    return ASCII_MAPS["default"]


def show_track_map(track: dict):
    """Display ASCII track map in a panel"""
    map_str = get_ascii_map(track["id"], track["name"])

    info_lines = [
        f"[bold yellow]📍 {track['name']}[/bold yellow]",
        f"[dim]{track['country']}[/dim]",
        "",
        f"[cyan]Length:[/cyan]  [white]{track['length_km']} km[/white]",
        f"[cyan]Corners:[/cyan] [white]{track.get('corners', 'N/A')}[/white]",
    ]
    if "drs_zones" in track:
        info_lines.append(f"[cyan]DRS:[/cyan]     [white]{track['drs_zones']} zones[/white]")
    if track.get("type") == "rally":
        info_lines.append(f"[cyan]Surface:[/cyan] [white]{track.get('surface', 'mixed')}[/white]")
        info_lines.append(f"[cyan]Cond:[/cyan]    [white]{track.get('conditions', 'N/A')}[/white]")

    map_panel = Panel(
        f"[dim white]{map_str}[/dim white]",
        title="[yellow]Track Map[/yellow]",
        border_style="yellow dim",
        padding=(0, 1),
    )

    info_text = Text.from_markup("\n".join(info_lines))
    info_panel = Panel(
        info_text,
        title="[cyan]Track Info[/cyan]",
        border_style="cyan dim",
        padding=(0, 1),
    )

    console.print(Columns([map_panel, info_panel], equal=False))
    console.print()


def select_category() -> str | None:
    """Category selection screen"""
    print_section_header("SELECT CATEGORY", "Choose a racing class")

    categories = list(CATEGORY_LABELS.items())
    table = Table(
        show_header=False,
        box=box.SIMPLE,
        padding=(0, 2),
        show_edge=False,
    )
    table.add_column("Num", style="bold red", width=4)
    table.add_column("Category", style="bold white", width=20)
    table.add_column("Cars", style="dim", width=40)
    table.add_column("Tracks", style="dim cyan", width=10)

    descriptions = {
        "f1":    "Single-seater open-wheel Formula cars",
        "gt3":   "High-performance GT endurance racing",
        "gt4":   "Entry-level GT production racing",
        "rally": "Off-road/mixed surface stage racing",
    }

    for i, (cat_id, cat_name) in enumerate(categories, 1):
        car_count = len(CARS.get(cat_id, []))
        track_count = len(TRACKS.get(cat_id, []))
        color = CATEGORY_COLORS.get(cat_id, "white")
        table.add_row(
            f"[bold red]{i}[/bold red]",
            f"[{color}]{cat_name}[/{color}]",
            f"[dim]{descriptions[cat_id]}[/dim]",
            f"[cyan]{track_count} tracks[/cyan]",
        )

    table.add_row("", "", "", "")
    table.add_row("[dim]B[/dim]", "[dim]← Back / Exit[/dim]", "", "")

    console.print(table)
    console.print()

    while True:
        choice = console.input("[bold red]▸[/bold red] [white]Select category:[/white] ").strip().upper()
        if choice == "B":
            return None
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(categories):
                return categories[idx][0]
        except ValueError:
            pass
        console.print("[red]Invalid choice. Try again.[/red]")


def select_track(category: str) -> dict | None:
    """Track selection screen with grouping"""
    cat_label = CATEGORY_LABELS[category]
    cat_color = CATEGORY_COLORS.get(category, "white")
    tracks = TRACKS.get(category, [])

    print_section_header(
        f"SELECT TRACK",
        f"[{cat_color}]{cat_label}[/{cat_color}] — {len(tracks)} circuits available"
    )

    table = Table(
        show_header=True,
        box=box.SIMPLE_HEAD,
        padding=(0, 2),
        header_style="bold red",
        show_edge=False,
    )
    table.add_column("#", style="bold red", width=4)
    table.add_column("Circuit", style="bold white", width=38)
    table.add_column("Country", style="dim cyan", width=18)
    table.add_column("Length", style="yellow", width=10)
    if category != "rally":
        table.add_column("Corners", style="dim", width=8)
    else:
        table.add_column("Surface", style="dim", width=12)

    for i, track in enumerate(tracks, 1):
        if category == "rally":
            extra = track.get("surface", "gravel").title()
        else:
            extra = str(track.get("corners", "–"))

        table.add_row(
            f"[bold red]{i}[/bold red]",
            track["name"],
            track["country"],
            f"{track['length_km']} km",
            extra,
        )

    console.print(table)
    console.print()
    console.print("[dim]  B → Back to categories[/dim]")
    console.print()

    while True:
        choice = console.input("[bold red]▸[/bold red] [white]Select track:[/white] ").strip().upper()
        if choice == "B":
            return None
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(tracks):
                selected = tracks[idx]
                clear()
                print_banner()
                show_track_map(selected)
                return selected
        except ValueError:
            pass
        console.print("[red]Invalid choice. Try again.[/red]")


def select_car(category: str) -> dict | None:
    """Car selection screen with specs table"""
    cat_label = CATEGORY_LABELS[category]
    cat_color = CATEGORY_COLORS.get(category, "white")
    cars = CARS.get(category, [])

    print_section_header(
        "SELECT CAR",
        f"[{cat_color}]{cat_label}[/{cat_color}]"
    )

    table = Table(
        show_header=True,
        box=box.SIMPLE_HEAD,
        padding=(0, 2),
        header_style="bold red",
        show_edge=False,
    )
    table.add_column("#", style="bold red", width=4)
    table.add_column("Car", style="bold white", width=28)
    table.add_column("Power", style="yellow", width=10)
    table.add_column("Weight", style="cyan", width=10)
    table.add_column("Drive", style="dim", width=6)
    table.add_column("Downforce", style="dim green", width=10)

    for i, car in enumerate(cars, 1):
        downforce_colors = {"extreme": "red", "medium": "yellow", "low": "green"}
        df_color = downforce_colors.get(car["downforce"], "white")
        table.add_row(
            f"[bold red]{i}[/bold red]",
            car["name"],
            f"[yellow]{car['power_hp']} hp[/yellow]",
            f"[cyan]{car['weight_kg']} kg[/cyan]",
            car["drivetrain"],
            f"[{df_color}]{car['downforce'].title()}[/{df_color}]",
        )

    console.print(table)
    console.print()
    console.print("[dim]  B → Back to tracks[/dim]")
    console.print()

    while True:
        choice = console.input("[bold red]▸[/bold red] [white]Select car:[/white] ").strip().upper()
        if choice == "B":
            return None
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(cars):
                return cars[idx]
        except ValueError:
            pass
        console.print("[red]Invalid choice. Try again.[/red]")


def run_prediction_animation(car_name: str, track_name: str):
    """Animated prediction progress bar"""
    console.print()
    console.print(f"  [dim]Calculating lap time for[/dim] [bold white]{car_name}[/bold white] [dim]at[/dim] [bold yellow]{track_name}[/bold yellow]")
    console.print()

    with Progress(
        SpinnerColumn(style="bold red"),
        TextColumn("[bold white]{task.description}"),
        BarColumn(bar_width=40, style="red", complete_style="bold red"),
        TextColumn("[bold red]{task.percentage:>3.0f}%"),
        console=console,
    ) as progress:
        task = progress.add_task("  Analysing track characteristics...", total=100)
        for i in range(35):
            time.sleep(0.02)
            progress.update(task, advance=1)

        progress.update(task, description="  Applying vehicle performance model...")
        for i in range(35):
            time.sleep(0.02)
            progress.update(task, advance=1)

        progress.update(task, description="  Computing predicted lap time...      ")
        for i in range(30):
            time.sleep(0.02)
            progress.update(task, advance=1)

    console.print()


def show_results(result: dict, car: dict, track: dict, category: str):
    """Display prediction results in a styled panel"""
    cat_color = CATEGORY_COLORS.get(category, "white")
    cat_label = CATEGORY_LABELS[category]
    is_rally = result.get("is_rally", False)

    console.print(Rule(style="red"))
    console.print()

    # Main result header
    if is_rally:
        time_label = "STAGE TIME"
        time_value = result["stage_time_formatted"]
    else:
        time_label = "PREDICTED LAP TIME"
        time_value = result["lap_time_formatted"]

    header = Text()
    header.append(f"  {time_label}\n", style="dim white")
    header.append(f"  {time_value}", style="bold green" + " on default")

    console.print(Panel(
        Align.center(
            Text.assemble(
                Text(f"\n  {time_label}  \n", style="dim white"),
                Text(f"  {time_value}  \n", style="bold green"),
                Text(f"\n  {car['name']}  ·  {track['name']}  \n", style="dim"),
            )
        ),
        border_style="green",
        box=box.DOUBLE,
        padding=(0, 4),
    ))

    console.print()

    # Sector breakdown
    sector_table = Table(
        show_header=True,
        box=box.SIMPLE_HEAD,
        header_style="bold white",
        padding=(0, 3),
        show_edge=False,
    )

    if is_rally:
        sector_table.add_column("Stage 1", style="bold green", justify="center")
        sector_table.add_column("Stage 2", style="bold yellow", justify="center")
        sector_table.add_column("Stage 3", style="bold red", justify="center")
        sector_table.add_row(
            result["ss1_formatted"],
            result["ss2_formatted"],
            result["ss3_formatted"],
        )
    else:
        sector_table.add_column("Sector 1", style="bold green", justify="center")
        sector_table.add_column("Sector 2", style="bold yellow", justify="center")
        sector_table.add_column("Sector 3", style="bold cyan", justify="center")
        sector_table.add_row(
            result["sector_1_formatted"],
            result["sector_2_formatted"],
            result["sector_3_formatted"],
        )

    console.print(Panel(
        Align.center(sector_table),
        title="[bold white]Sector Breakdown[/bold white]",
        border_style="dim white",
        padding=(0, 2),
    ))

    console.print()

    # Speed & car stats side by side
    speed_table = Table(show_header=False, box=box.SIMPLE, padding=(0, 3), show_edge=False)
    speed_table.add_column("Label", style="dim cyan", width=16)
    speed_table.add_column("Value", style="bold white", width=16)
    speed_table.add_row("Top Speed", f"[bold yellow]{result['top_speed_kmh']} km/h[/bold yellow]")
    speed_table.add_row("Avg Speed", f"[white]{result['avg_speed_kmh']} km/h[/white]")
    speed_table.add_row("Confidence", f"[dim]{result['confidence']}[/dim]")

    car_table = Table(show_header=False, box=box.SIMPLE, padding=(0, 3), show_edge=False)
    car_table.add_column("Label", style="dim cyan", width=16)
    car_table.add_column("Value", style="bold white", width=16)
    car_table.add_row("Power",  f"[yellow]{car['power_hp']} hp[/yellow]")
    car_table.add_row("Weight", f"[cyan]{car['weight_kg']} kg[/cyan]")
    car_table.add_row("Drive",  car["drivetrain"])

    console.print(Columns([
        Panel(speed_table, title="[yellow]Speed Data[/yellow]", border_style="yellow dim"),
        Panel(car_table,   title="[cyan]Car Specs[/cyan]",    border_style="cyan dim"),
    ]))

    console.print()
    console.print(Rule(style="red dim"))


def show_compare_menu() -> str:
    """Show options after prediction"""
    console.print()
    options = Table(show_header=False, box=None, padding=(0, 2))
    options.add_column("Key",  style="bold red",   width=4)
    options.add_column("Action", style="dim white", width=30)

    options.add_row("[1]", "Predict another car (same track)")
    options.add_row("[2]", "Change track (same category)")
    options.add_row("[3]", "Change category")
    options.add_row("[4]", "Start over")
    options.add_row("[Q]", "Quit")

    console.print(options)
    console.print()
    return console.input("[bold red]▸[/bold red] [white]Choice:[/white] ").strip().upper()


def main():
    """Main application loop"""
    print_banner()

    category = None
    track = None

    while True:
        # ── Category ────────────────────────────────────────
        if category is None:
            category = select_category()
            if category is None:
                console.print("\n[dim]Goodbye. Keep the rubber side down. 🏁[/dim]\n")
                sys.exit(0)
            track = None

        # ── Track ────────────────────────────────────────────
        if track is None:
            clear()
            print_banner()
            result_track = select_track(category)
            if result_track is None:
                category = None
                continue
            track = result_track

        # ── Car ──────────────────────────────────────────────
        car = select_car(category)
        if car is None:
            track = None
            continue

        # ── Prediction ───────────────────────────────────────
        run_prediction_animation(car["name"], track["name"])
        result = predict_lap_time(category, track["id"], car["id"])

        if "error" in result:
            console.print(f"[red]Prediction error: {result['error']}[/red]")
        else:
            show_results(result, car, track, category)

        # ── Post-result menu ─────────────────────────────────
        choice = show_compare_menu()

        if choice == "1":
            continue  # same track, pick new car
        elif choice == "2":
            track = None
            continue
        elif choice == "3":
            category = None
            track = None
            clear()
            print_banner()
            continue
        elif choice == "4":
            category = None
            track = None
            clear()
            print_banner()
            continue
        elif choice == "Q":
            console.print("\n[dim]Goodbye. Keep the rubber side down. 🏁[/dim]\n")
            sys.exit(0)
        else:
            console.print("[red]Invalid choice, picking new car.[/red]")


if __name__ == "__main__":
    main()
