"""
Core data definitions for the Lap Time Predictor.
Tracks, cars, and their specifications.
"""

TRACKS = {
    "f1": [
        {"id": "albert_park", "name": "Albert Park Circuit", "country": "Australia", "length_km": 5.278, "corners": 16, "drs_zones": 3, "elevation_m": 10, "surface": "tarmac", "type": "street_park"},
        {"id": "shanghai", "name": "Shanghai International Circuit", "country": "China", "length_km": 5.451, "corners": 16, "drs_zones": 2, "elevation_m": 5, "surface": "tarmac", "type": "permanent"},
        {"id": "suzuka", "name": "Suzuka International Racing Course", "country": "Japan", "length_km": 5.807, "corners": 18, "drs_zones": 2, "elevation_m": 42, "surface": "tarmac", "type": "permanent"},
        {"id": "bahrain", "name": "Bahrain International Circuit", "country": "Bahrain", "length_km": 5.412, "corners": 15, "drs_zones": 3, "elevation_m": 8, "surface": "tarmac", "type": "permanent"},
        {"id": "jeddah", "name": "Jeddah Corniche Circuit", "country": "Saudi Arabia", "length_km": 6.174, "corners": 27, "drs_zones": 3, "elevation_m": 3, "surface": "tarmac", "type": "street"},
        {"id": "miami", "name": "Miami International Autodrome", "country": "USA", "length_km": 5.412, "corners": 19, "drs_zones": 3, "elevation_m": 2, "surface": "tarmac", "type": "street_park"},
        {"id": "montreal", "name": "Circuit Gilles Villeneuve", "country": "Canada", "length_km": 4.361, "corners": 14, "drs_zones": 2, "elevation_m": 5, "surface": "tarmac", "type": "street_park"},
        {"id": "monaco", "name": "Circuit de Monaco", "country": "Monaco", "length_km": 3.337, "corners": 19, "drs_zones": 1, "elevation_m": 42, "surface": "tarmac", "type": "street"},
        {"id": "barcelona", "name": "Circuit de Barcelona-Catalunya", "country": "Spain", "length_km": 4.657, "corners": 14, "drs_zones": 2, "elevation_m": 30, "surface": "tarmac", "type": "permanent"},
        {"id": "red_bull_ring", "name": "Red Bull Ring", "country": "Austria", "length_km": 4.318, "corners": 10, "drs_zones": 3, "elevation_m": 65, "surface": "tarmac", "type": "permanent"},
        {"id": "silverstone", "name": "Silverstone Circuit", "country": "Great Britain", "length_km": 5.891, "corners": 18, "drs_zones": 2, "elevation_m": 15, "surface": "tarmac", "type": "permanent"},
        {"id": "spa", "name": "Circuit de Spa-Francorchamps", "country": "Belgium", "length_km": 7.004, "corners": 19, "drs_zones": 2, "elevation_m": 104, "surface": "tarmac", "type": "permanent"},
        {"id": "hungaroring", "name": "Hungaroring", "country": "Hungary", "length_km": 4.381, "corners": 14, "drs_zones": 1, "elevation_m": 35, "surface": "tarmac", "type": "permanent"},
        {"id": "zandvoort", "name": "Zandvoort", "country": "Netherlands", "length_km": 4.259, "corners": 14, "drs_zones": 2, "elevation_m": 8, "surface": "tarmac", "type": "permanent"},
        {"id": "monza", "name": "Autodromo Nazionale Monza", "country": "Italy", "length_km": 5.793, "corners": 11, "drs_zones": 2, "elevation_m": 10, "surface": "tarmac", "type": "permanent"},
        {"id": "baku", "name": "Baku City Circuit", "country": "Azerbaijan", "length_km": 6.003, "corners": 20, "drs_zones": 2, "elevation_m": 5, "surface": "tarmac", "type": "street"},
        {"id": "singapore", "name": "Marina Bay Street Circuit", "country": "Singapore", "length_km": 4.940, "corners": 19, "drs_zones": 3, "elevation_m": 3, "surface": "tarmac", "type": "street"},
        {"id": "cota", "name": "Circuit of the Americas", "country": "USA", "length_km": 5.513, "corners": 20, "drs_zones": 2, "elevation_m": 40, "surface": "tarmac", "type": "permanent"},
        {"id": "mexico", "name": "Autodromo Hermanos Rodriguez", "country": "Mexico", "length_km": 4.304, "corners": 17, "drs_zones": 3, "elevation_m": 2285, "surface": "tarmac", "type": "permanent"},
        {"id": "interlagos", "name": "Interlagos", "country": "Brazil", "length_km": 4.309, "corners": 15, "drs_zones": 2, "elevation_m": 785, "surface": "tarmac", "type": "permanent"},
        {"id": "las_vegas", "name": "Las Vegas Strip Circuit", "country": "USA", "length_km": 6.201, "corners": 17, "drs_zones": 3, "elevation_m": 620, "surface": "tarmac", "type": "street"},
        {"id": "qatar", "name": "Lusail International Circuit", "country": "Qatar", "length_km": 5.380, "corners": 16, "drs_zones": 2, "elevation_m": 5, "surface": "tarmac", "type": "permanent"},
        {"id": "abu_dhabi", "name": "Yas Marina Circuit", "country": "Abu Dhabi", "length_km": 5.281, "corners": 16, "drs_zones": 2, "elevation_m": 3, "surface": "tarmac", "type": "permanent"},
    ],
    "gt3": [
        {"id": "spa_gt3", "name": "Circuit de Spa-Francorchamps", "country": "Belgium", "length_km": 7.004, "corners": 19, "elevation_m": 104, "surface": "tarmac", "type": "permanent"},
        {"id": "paul_ricard", "name": "Circuit Paul Ricard", "country": "France", "length_km": 5.842, "corners": 15, "elevation_m": 10, "surface": "tarmac", "type": "permanent"},
        {"id": "suzuka_gt3", "name": "Suzuka International Racing Course", "country": "Japan", "length_km": 5.807, "corners": 18, "elevation_m": 42, "surface": "tarmac", "type": "permanent"},
        {"id": "red_bull_ring_gt3", "name": "Red Bull Ring", "country": "Austria", "length_km": 4.318, "corners": 10, "elevation_m": 65, "surface": "tarmac", "type": "permanent"},
        {"id": "barcelona_gt3", "name": "Circuit de Barcelona-Catalunya", "country": "Spain", "length_km": 4.657, "corners": 14, "elevation_m": 30, "surface": "tarmac", "type": "permanent"},
        {"id": "donington", "name": "Donington Park", "country": "UK", "length_km": 4.020, "corners": 12, "elevation_m": 25, "surface": "tarmac", "type": "permanent"},
        {"id": "oulton_park", "name": "Oulton Park", "country": "UK", "length_km": 4.307, "corners": 20, "elevation_m": 30, "surface": "tarmac", "type": "permanent"},
        {"id": "snetterton", "name": "Snetterton Circuit", "country": "UK", "length_km": 4.779, "corners": 13, "elevation_m": 5, "surface": "tarmac", "type": "permanent"},
        {"id": "hockenheim", "name": "Hockenheimring", "country": "Germany", "length_km": 4.574, "corners": 17, "elevation_m": 10, "surface": "tarmac", "type": "permanent"},
        {"id": "oschersleben", "name": "Motorsport Arena Oschersleben", "country": "Germany", "length_km": 3.696, "corners": 15, "elevation_m": 15, "surface": "tarmac", "type": "permanent"},
        {"id": "imola", "name": "Autodromo Enzo e Dino Ferrari", "country": "Italy", "length_km": 4.909, "corners": 22, "elevation_m": 20, "surface": "tarmac", "type": "permanent"},
        {"id": "watkins_glen", "name": "Watkins Glen International", "country": "USA", "length_km": 5.550, "corners": 11, "elevation_m": 55, "surface": "tarmac", "type": "permanent"},
        {"id": "road_america", "name": "Road America", "country": "USA", "length_km": 6.515, "corners": 14, "elevation_m": 35, "surface": "tarmac", "type": "permanent"},
        {"id": "road_atlanta", "name": "Michelin Raceway Road Atlanta", "country": "USA", "length_km": 4.088, "corners": 12, "elevation_m": 45, "surface": "tarmac", "type": "permanent"},
        {"id": "beijing", "name": "Beijing E-Town Street Circuit", "country": "China", "length_km": 4.015, "corners": 16, "elevation_m": 5, "surface": "tarmac", "type": "street"},
    ],
    "gt4": [
        {"id": "paul_ricard_gt4", "name": "Circuit Paul Ricard", "country": "France", "length_km": 5.842, "corners": 15, "elevation_m": 10, "surface": "tarmac", "type": "permanent"},
        {"id": "zandvoort_gt4", "name": "Circuit Zandvoort", "country": "Netherlands", "length_km": 4.259, "corners": 14, "elevation_m": 8, "surface": "tarmac", "type": "permanent"},
        {"id": "spa_gt4", "name": "Circuit de Spa-Francorchamps", "country": "Belgium", "length_km": 7.004, "corners": 19, "elevation_m": 104, "surface": "tarmac", "type": "permanent"},
        {"id": "misano", "name": "Misano World Circuit", "country": "Italy", "length_km": 4.226, "corners": 16, "elevation_m": 10, "surface": "tarmac", "type": "permanent"},
        {"id": "nurburgring", "name": "Nurburgring GP Circuit", "country": "Germany", "length_km": 5.148, "corners": 15, "elevation_m": 60, "surface": "tarmac", "type": "permanent"},
        {"id": "barcelona_gt4", "name": "Circuit de Barcelona-Catalunya", "country": "Spain", "length_km": 4.657, "corners": 14, "elevation_m": 30, "surface": "tarmac", "type": "permanent"},
        {"id": "donington_gt4", "name": "Donington Park", "country": "UK", "length_km": 4.020, "corners": 12, "elevation_m": 25, "surface": "tarmac", "type": "permanent"},
        {"id": "oulton_park_gt4", "name": "Oulton Park", "country": "UK", "length_km": 4.307, "corners": 20, "elevation_m": 30, "surface": "tarmac", "type": "permanent"},
        {"id": "snetterton_gt4", "name": "Snetterton Circuit", "country": "UK", "length_km": 4.779, "corners": 13, "elevation_m": 5, "surface": "tarmac", "type": "permanent"},
        {"id": "watkins_glen_gt4", "name": "Watkins Glen International", "country": "USA", "length_km": 5.550, "corners": 11, "elevation_m": 55, "surface": "tarmac", "type": "permanent"},
        {"id": "road_america_gt4", "name": "Road America", "country": "USA", "length_km": 6.515, "corners": 14, "elevation_m": 35, "surface": "tarmac", "type": "permanent"},
    ],
    "rally": [
        {"id": "monte_carlo", "name": "Rallye Monte-Carlo", "country": "Monaco/France", "length_km": 330, "surface": "mixed", "type": "rally", "conditions": "mixed tarmac/ice", "avg_elevation_m": 800},
        {"id": "rally_sweden", "name": "Rally Sweden", "country": "Sweden", "length_km": 290, "surface": "snow", "type": "rally", "conditions": "snow and ice", "avg_elevation_m": 300},
        {"id": "safari_kenya", "name": "Safari Rally Kenya", "country": "Kenya", "length_km": 380, "surface": "gravel", "type": "rally", "conditions": "rough gravel/dust", "avg_elevation_m": 1700},
        {"id": "rally_finland", "name": "Rally Finland", "country": "Finland", "length_km": 320, "surface": "gravel", "type": "rally", "conditions": "fast forest gravel", "avg_elevation_m": 150},
        {"id": "rally_sardegna", "name": "Rally Italia Sardegna", "country": "Italy", "length_km": 300, "surface": "gravel", "type": "rally", "conditions": "rocky gravel", "avg_elevation_m": 400},
        {"id": "rally_portugal", "name": "Rally de Portugal", "country": "Portugal", "length_km": 310, "surface": "gravel", "type": "rally", "conditions": "flowing gravel", "avg_elevation_m": 300},
        {"id": "wales_rally", "name": "Wales Rally GB", "country": "Great Britain", "length_km": 295, "surface": "gravel", "type": "rally", "conditions": "wet forest gravel", "avg_elevation_m": 350},
        {"id": "rally_japan", "name": "Rally Japan", "country": "Japan", "length_km": 285, "surface": "mixed", "type": "rally", "conditions": "mixed gravel/tarmac", "avg_elevation_m": 500},
        {"id": "rally_argentina", "name": "Rally Argentina", "country": "Argentina", "length_km": 340, "surface": "gravel", "type": "rally", "conditions": "high altitude gravel", "avg_elevation_m": 1200},
        {"id": "ypres_rally", "name": "Ypres Rally Belgium", "country": "Belgium", "length_km": 270, "surface": "tarmac", "type": "rally", "conditions": "narrow fast tarmac", "avg_elevation_m": 50},
    ]
}

CARS = {
    "f1": [
        {"id": "rb19", "name": "Red Bull RB19", "weight_kg": 798, "power_hp": 1000, "drivetrain": "RWD", "downforce": "extreme", "tire_type": "slick"},
        {"id": "sf23", "name": "Ferrari SF-23", "weight_kg": 810, "power_hp": 980, "drivetrain": "RWD", "downforce": "extreme", "tire_type": "slick"},
        {"id": "w14", "name": "Mercedes W14", "weight_kg": 805, "power_hp": 985, "drivetrain": "RWD", "downforce": "extreme", "tire_type": "slick"},
        {"id": "mcl60", "name": "McLaren MCL60", "weight_kg": 807, "power_hp": 975, "drivetrain": "RWD", "downforce": "extreme", "tire_type": "slick"},
        {"id": "a523", "name": "Alpine A523", "weight_kg": 812, "power_hp": 970, "drivetrain": "RWD", "downforce": "extreme", "tire_type": "slick"},
    ],
    "gt3": [
        {"id": "porsche_gt3r", "name": "Porsche 911 GT3 R", "weight_kg": 1270, "power_hp": 550, "drivetrain": "RWD", "downforce": "medium", "tire_type": "slick"},
        {"id": "ferrari_488_gt3", "name": "Ferrari 488 GT3", "weight_kg": 1245, "power_hp": 600, "drivetrain": "RWD", "downforce": "medium", "tire_type": "slick"},
        {"id": "amg_gt3", "name": "Mercedes-AMG GT3", "weight_kg": 1320, "power_hp": 585, "drivetrain": "RWD", "downforce": "medium", "tire_type": "slick"},
        {"id": "r8_gt3", "name": "Audi R8 LMS GT3", "weight_kg": 1280, "power_hp": 585, "drivetrain": "RWD", "downforce": "medium", "tire_type": "slick"},
        {"id": "m4_gt3", "name": "BMW M4 GT3", "weight_kg": 1300, "power_hp": 585, "drivetrain": "RWD", "downforce": "medium", "tire_type": "slick"},
    ],
    "gt4": [
        {"id": "cayman_gt4", "name": "Porsche 718 Cayman GT4", "weight_kg": 1360, "power_hp": 420, "drivetrain": "RWD", "downforce": "low", "tire_type": "slick"},
        {"id": "m4_gt4", "name": "BMW M4 GT4", "weight_kg": 1410, "power_hp": 430, "drivetrain": "RWD", "downforce": "low", "tire_type": "slick"},
        {"id": "amg_gt4", "name": "Mercedes AMG GT4", "weight_kg": 1400, "power_hp": 430, "drivetrain": "RWD", "downforce": "low", "tire_type": "slick"},
        {"id": "vantage_gt4", "name": "Aston Martin Vantage GT4", "weight_kg": 1430, "power_hp": 430, "drivetrain": "RWD", "downforce": "low", "tire_type": "slick"},
        {"id": "a110_gt4", "name": "Alpine A110 GT4", "weight_kg": 1325, "power_hp": 420, "drivetrain": "RWD", "downforce": "low", "tire_type": "slick"},
    ],
    "rally": [
        {"id": "fiesta_wrc", "name": "Ford Fiesta WRC", "weight_kg": 1200, "power_hp": 380, "drivetrain": "AWD", "downforce": "low", "tire_type": "rally"},
        {"id": "yaris_rally1", "name": "Toyota GR Yaris Rally1", "weight_kg": 1250, "power_hp": 380, "drivetrain": "AWD", "downforce": "low", "tire_type": "rally"},
        {"id": "i20_rally1", "name": "Hyundai i20 N Rally1", "weight_kg": 1230, "power_hp": 380, "drivetrain": "AWD", "downforce": "low", "tire_type": "rally"},
        {"id": "c3_rally2", "name": "Citroen C3 Rally2", "weight_kg": 1320, "power_hp": 280, "drivetrain": "AWD", "downforce": "low", "tire_type": "rally"},
        {"id": "fabia_rally2", "name": "Skoda Fabia Rally2", "weight_kg": 1330, "power_hp": 280, "drivetrain": "AWD", "downforce": "low", "tire_type": "rally"},
    ]
}

CATEGORY_LABELS = {
    "f1": "Formula 1",
    "gt3": "GT3",
    "gt4": "GT4",
    "rally": "Rally"
}

ASCII_MAPS = {
    # ── F1 Tracks ─────────────────────────────────────────────────────────
    "albert_park": """
......................-===-:..........................
...............-#@%+-:-+#@@=:.........................
.............#@*...........-%@+.......................
........%@@@*:................-@@:....................
......:@+.......................:*@-..................
......*%..........................:%*................
.....-@:...........................:@................
.....%*............................-@................
....#%..............................%+...............
...+@:..............................:@=..............
...%#.................................%*.............
..:@=..................................*@:...........
..=@.....................................@%:.......-%@@@@@@@##**#@@@%-
..+%......................................:#@+....#@=.................-%@#:
..:%#........................................=@@*-..........=*%@=...........+@%+
....=@*.........................................:=*#%%%%%#*+-:...............=%@+:
......*@+.....................................................................-%%:
........#@-.......................................................................@+
.........%%....................................................................*@:
.......:@*.....................................................................-@-
......:@+...................................................................:@=
......:@#-:.......................................................................:@+
.........:+@@@@#+:.............................................................*@#@@@@*-...+@-
................::=*#%@@@@@@@@@@@@@@@@@%=..........................................*@.....:-*%@+
.....................................+@-........................................*@.
.....................................=@-.................................:...::=@:
......................................:+##%%%%%%%%%%%%%%%%%%%%%%%%%########**+=
""",

    "shanghai": """
                                .=@@%#*#@@#..
                             .:@#..     .+@=.
                          . .-@*  ...     +@:.
                    .       :@# .-%@#-.  .+@-.
                          .#%  -@=.=@@-.=%*.
                         .*@:  .+#:. =#%#-.  ....:--===--:...
                        .-%=.   .*@+:...:-===++*#@@@@%#**+++**#@@#+=-:..
                        :*#:      :+*###**+++=-:...             ..=+*#@@*+=..
                       .=@-                                            .:=+%@=.
                      .-@+.                                              .-*@*.
                      .##:                   ..:=**######**************%@#=:
                      =@=                    .:#@+-:......::---=======-:..
                      .@#                     *@+.
                     .%%.        .           *@-.
                     +@-                    .@*.
                    :@#                     .@=
                   .#@.                      %%.
                  .*@:              .         @#.
                  :#+.                   .    :@*.
                 .+@-                     .   .-@+.
                .=@=          ..    .           -@+.
               .:%*. .                       .  .+@-.
               . .*%-                              :#=.
                 -@+          .       .            :%=.
              . .@#.             .               .:*%:.
             .*@:  .      .         -=**+=====+@%+:.
            .=@=   .               =@=::--=++=:..              .:==++=-.
            :%#                    .%#.  .    .               :*%*=--+*%#:.
           .*@.                    .+@-.                      -%+..    .*@-
          .=@-.      .              .#@++++=-:::....           .*#:      .##
          :#*.   . ..                .-====+++***#%%@@@@@@@@@@%%%%%###%%:.      *%
.:--=+****%%:                 .                      ......................      :%*
=@%=:...........                                                             .-#@+..
#@*+++++**************###########****************************************************######%@@%-..
.:---------:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::.......
""",

    "suzuka": """
     .=%#***#-..
     *+......#=...
     *=.......#-.
     .*+..  ..-#..                    .-##-
      .:**.....=#..    .    . . .   ..=#.#-
      . ..+#=...-#:.                .*#.#-..
   .  .    .:*#=..**.             ..**.=#.
         . . ...*%*.=%#-. . .  ...=%-..=*..
               ....:*%#=-*%%%%%%#=... .:#.         .  .+#.........  ....+%-.
                    ....:+##=.....  .  .#-.        ..*#...=#######-.... ..##...
         .             . ....:+##+:.....-*.      ..+#..-#=... .....+%-.....=%-...
            .  .           .     ..=*%*-:#:.....-%*..:%-.....    ....*-......##...
       .              ..   .. .   .... .=#%**##+:...**.......       .*=.......=%=.
        .         . . . .               .-*. .....-%:              .-#..      ..##:.
  . .               .     .              .**###%#*+.               .#:..        .=%=..
                                                                 . .#-..        ...##:..
  .   .                       .                     .     .        ..*#+-::.      ..-%+...
   . . .           .                              .               . ......:-#=.      .+#:.
        .           .            .                 .          ..  .        ..#-..     ..*+.
                    .            .                 .                     .  .-*...      .-#:..
   .          .   .                              .                         .  **.....   ...*+.
   .       .          .                                              .        ..+*###-... ..-#:..
     .   .           .         .        .             .             .         .  ....+*.. . ..#-.
          .    .                         .                 .        .       .        .=*..   .=*.
                  .            .      .               .                               .-#:. ..#-.
                                                      .     .             .            .:#=::*+..
""",

    "bahrain": """
         @@@@@@
        @@@  @@@@
        @@@    @@@@                                            @@@
       @@@       @@@@                                       @@@@@@@@
       @@@        @@@@                                     @@@    @@@
       @@@          @@@@                                 @@@@      @@@@
      @@@            @@@@@                              @@@@        @@@@
      @@@               @@@@@                           @@@          @@@@
      @@@                 @@@@@@@                      @@@             @@@
     @@@                      @@@@@                   @@@               @@@
     @@@                         @@@                 @@@                 @@@
     @@@                         @@@                 @@@                  @@@@
     @@@                         @@@                 @@@                   @@@@
    @@@                          @@@                 @@@                     @@@
    @@@                          @@@                  @@@                    @@@@
    @@@                          @@@@                  @@@@                    @@@@
    @@@                            @@@@@                 @@@@@@                 @@@@
   @@@@                              @@@@@                  @@@@@@@              @@@@
   @@@                                 @@@@@                    @@@@@@            @@@@
   @@@                                    @@@@@                     @@@@            @@@
   @@@                                      @@@@@                     @@@@          @@@@
  @@@               @@@@@@@@@                  @@@@                    @@@@           @@@
  @@@            @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                    @@@            @@@
  @@@          @@@@                 @@@@@@@@@@@@@@@                     @@@@            @@@@
  @@@         @@@@@                                                     @@@              @@@@
  @@@          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@               @@@@
  @@@                                @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                      @@@@
  @@@                                                                                       @@@@
   @@@                                                                                        @@@
    @@@                                                                                        @@@@
    @@@                                                                                         @@@
  @@@@                                                                                           @@@
@@@@@                                                                                            @@@
@@@                                                                                          @@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
""",

    "jeddah": """
                                                    .=*****++===--:::...
   .                                           . .. =*: ...::----===++***#####**++=-::...
    .                                        .    . .++.   .      . .  .     ....:---==+*##-
   .:*#-.                                         -#+.    .     ..          .          .=@
  .-+=:...-*:.-*+-:*:.                            =#: .          .     ...      . .     +%
:==--::::...:=+:  .:::.-+-.    .                  +#:              .                    +#
-++:  .=+.             .::.                    .  *@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+.
#.. ..#.                                         =*: ...::----===++***
-#+*#-. .
  .  .:.
  .  .:.
  -. .=.
  .#=*=.
  :+-.
  .+-.
  .*=.
  .#=:..
    .*@=.
    #%..
    -=
    #..
    -=
     *
""",

    "miami": """
               .@@@@%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%#*++=-::::...
     .          :#@@%-.  .    .+##%@@%##=.......::::---------==+**##%%%@@@@@@@@@@@@@@@@@@@@@@@@*
         .       .:#@@@+-::=*@@@@@%##%@@@@@#=..
                    .*@@@@@@@%+..     . .+%@@@@@=:.
      .     .         .......       ..     ..-@@@@@@*.
   . .              .                           .-#@@@@%*:         .-%@@@@@@@+.
           . .                    .     .           .=*@@@@@+:               :@@%*++=.
                                                        .-%@@@@:              -@@#.
          .  .   .     .      . . .                         =@@*..            .=@@@@+.
          .+#%%#+.          :*##=.                      ..%@@@*.
       .*@@@@@@@@@%.    .+@@@@@@@@@*:.                  .#@@-.               ..-@@@-.
      -@@@*.    -@@@%=+@@@@#:.  .*@@@@#:.               .%@%                  :%@@@@@*.
 .    %@%.        -@@@@@%.         .+@@@@%.  . .        .%@%                :%@@@@@=.
.     :#@@%-.   ....              .=@@@@@@*.
       .:#@@@+-::=*@@@@@%##%@@@@@#=..    +%@@@@@=:.
         ..*@@@@@@@%+..               .+%@@@@@*:
              ........       ..     ..-@@@@@@*.     .         :=*@@@@@+:.
                   .                  .-#@@@@%*:      .           .=*@@@@@+:
                                          .=*@@@@@+:                    .-%@@@@:
                                              .-%@@@@:              -@@#.
                                                  =@@*..            .=@@@@+.
 .   :*@@@*-...............:-*%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%##+-.
""",

    "montreal": """
     .....:=#@%%%###*+*@:................
   ....:*%#=...........-%%@@@%###@%%%%=:...
  ...=%#:....  .      ................+%#:....
  ..-%-.-=-:...   .                  ...-#*:....:-==-.....
  ...=##+=+#=...     .      .          ...-%*:.+%+-=+%*=....
    .......-#*:...                .      ...=#%+:.....:*%+:...
          ...+%+....                       .......    ..:=%*:...
           ....=%*-....      .                .        ....-%#-...
             ....-##=....                                 ...-##-...
                ...:+%#+.....                               ...-#*:..
                  ....:-%#=....         .       .             ...=#+...
                     ....:=##+....           .      .      .   ...:#%:..
  .                     ....:-@#*.....          .                ...-@=...
                           .....-#%+....                    .      ...%#...
                    .        ......:#%*..        .                  ..:%*...
                 .                ....@+.. .    .                     ..+#:..
                   .       .        ..:@%-....              .   .  .  ...+#:.
                  .     .            ....+@@-.....           .        ..-%+..
    .         ..                       .....+%@-:....                ...=#:..
                                     .     ....=%%=:....              ..:#+...
    ..  .                   .   .             ....+#@-:....            ..:#+...
                                                .....=#%+:....          ...##...
             ..                              .  .   ....=#%+:....   .    ...*%-...
   .      .                                   .       .....=*@=-.....     ...=%=...
           .               .             .               .....-*%+-....     ..:#*:...
       .                                 .                   ....-*%+-.....  ..:+#-...
      .              ..    .   .        .                      .....-+%#+-.......-#*:...
                                       .     .     .           .   ....:-+#%*+:....=%*:...
                                                                      ......:=+%#*=..=%#-....
                  .   . .                                                 .......:=*@%###%#-....
     .                                             ..            .            ........:-*%#+@#-...
                        .  .         .              . .  .  .   .                   ......-%%%#:..
                                                      .                  .              .....:....
""",

    "monaco": """
        .      ..             ..-+***+..
        .         .        ..-*#=....=*-..
    .                   ..:*#=.-*#%%*=-*+..
.      .               .=%=.:##:   ..-#*=#=.
    .         .     .:*#:.:**..      ..-#*+#-.
       .          .:**:..:++.          ..=#++#=.
                ..+*:.  .-#-.     .     ...=*==*+:.
               .-#=.. .:**:. .             .:+*-:+*+-..         .:+*+++++++++++++*-.
        .   ...+#..-::+*:                 .  .=*-..:=**-..        .*=.... ...    .-#=.
           ...+*.:#+=+-.       .              .-+**+:.:+*=..      .*=..    .   ..*@##*=:..
     .     ..+*.:#-          ..  .          .     .-**=:.=*=:.. ..+*:..      . .*=%-..-#+.
    .     ..-%.:%-           ..      .               .-**-.-##**##=..          .*#*:..=%=.
         ..:*+.-#.        .                             .-#*-..                   .:*#:..
         .:%:..=*             .                   .     ....=#*:..    .        ..+%+...
    .    ..:+#:-#                                           ..:=*##+-.....:-=*##=:.....
           ..:++-                                              ....:--====--::.....
""",

    "barcelona": """
      .:-+*##%###################*-.            ....::...    .
   .-*%#*=:. .   .    .         .+%+..        ..=#%%##%%*-..                .   .=*#%#+-:.....
 .:%%=.      .         .   . .   .=#:.       .=#*:.    .-#%*-...    .          -%*:. .-*#%@#=-.....
.=@=       .      .      .  .    .+#:      ..+%=.         .:#@#-...           .#=.   .    ..-#@@#..
=@:. .                      .   .-%+.      :*#-.  .         ..:*@%-.     ..   .#=.        .   ..@=.
%*.        .   .            ...+%#-. ... .-#*:. .          .   ..:*%%=..   .  .=%*:.           .@=.
@=..       .-#%%%%%%%%%%%%%%%%*=:.      .=%+..              .     ..-+%#=..    .:=#%#+:..  .  .-@-.
%#.  .. . .:@+................ .. .    .+%=. .        .  .   . .      .-+%#=:. .  ..:%*..      +@:.
:@*.      ..#%=:     .      .        .:*#-.             .       . .. .   .:+%#+:.   .:%=.     .*@:..
 :#%=:.   . .:*%*-.  ...             :*#:    .           .     .            .:+%#=:.. +@-..    :*#%*
   :*%%*-:..  ..-#%+:. .   .  .   .  -#*.            .   .      ..        .. .. :+%%=:.##..  .   .=@
.     .:*%@#:.   ..=%%=:...         .-%+. .    .   .      .             . .        .+%@%%:..   .  =@
 . ..     .:%#.      .=@@@#+-:....::-##:...   ..   .                 .             .    ..        =@
 .         .-@-.     .....:::--------:..            . .   .   .   ..       .      .   .           *%
 ..  .     .:@=  .           .   .  .          ..  ..       .. . .        .           . .  .  . .-@=.
 .       . ..#%:          .    .  .     .         .     ...                .   ..      .  . . .-*@=.
            ..=#%####%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%###############################%#=:.
""",

    "red_bull_ring": """
+%@@%%#**=-..
#%-...:-+#%@@@@%+:
.@#:         ..=*%@@%+:..
.-%%.           . ..-+%@@*=:.
 .-%@:                ..:=%@@#=.
   :@%:.              .    ..=@@@#:..
   ..%%:.             .   .    .:+#@@*-.
     :%@:         .             .  .-+%@%*:
     .:%@:                ..          ..:*@@@*:.
       :@@-                    .  .         :#%@@#-:..
       ..%%:                         . .        :=*%@@*+-..
  .      :%%.   .                                   .:-*@@@%%=..
 .    .   -@#.                     .             .         .+%@@@@+:..
       .  .+@+           .     .  .    .                         -*#@%:.
           .%@-    .        ..:=+=:. .                           .  :@%.
            -@*.    .     .+@@%*+#@@@@=.                     .      *@%..
            .@%: .   .. .-@#:       .=#@@%=:.      .   .         .:#@*
             =@=  .     :%%.       ..  ..=*@@%+-.   .         .-+@@+..
             :@+.       =@#                 .:+@@@%%=:...:-#%%@@=:.
             .#%:       :%%  .           .        .=%%%%%%%*.
             .+@-    .  .%@:
 .       .   .-@+        =@*  .     .
        .     :#%    .   .@%:
  ..          .*@:   .    -@+.
               :%@. .     .=@+      .          .+####*-.
                *@+        .*@.  .      ..:@@@@%%=--=#%%@@@@@+::..
               .:@#.        :%@:    .  :*@%*..      ..   ...-**#@@@%+==:.
                 *@=         :#@#=::=#@@#:.                     ...-=+#@@@%#*=.
   .             .@#:          .:#@@*:.                                ..:=@@@@@@%=.
    ...           +@-.                   .                  .                   ..:+#%%@@@*-:..
                  :#%.                                                       ..:=+#@@%+:
                  .=@*.                                                             ...:%@=.
. .            .   .#@:                                                                . .*@:
                 .  :@%.                                                                   .-@+
              .     .+@+                                                                    -%*
                     .%@-                                                                   :%#
                    . :@#.                                                                  :%%
                      .=@+                                                                  :#@
                       .#@:                                                                 .#@
       .                :%@.                                                                :#@
                        .=@*..                                                              :%#
                 .       .%@=                                                              .*@-
         .. .   ..        :@*................................................................:+@@%-.
                          .-*%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%##+-.
""",

    "silverstone": """
         @@@@@@@@@@@@@@@
       @@@@@    @@@@@@@@@@@@@@@
      @@@                  @@@@@@@@@@@@ @@@@@@@
     @@@                           @@@@@@@@@@@@@@@
    @@@                                         @@@@     @@@@@
    @@@                                           @@@@@@@@@@@@@@@
   @@@                                                         @@@
   @@@                                       @@                 @@
  @@@@                                    @@@@@@@@@             @@@
  @@@                                 @@@@@@    @@@@@@           @@@
  @@@                              @@@@@@          @@@@          @@@@
 @@@                            @@@@@        @@@@@@@@@@@           @@@
 @@@                         @@@@@          @@@@                    @@@@
 @@@                      @@@@@              @@@                      @@@@
@@@                   @@@@@@                 @@@                        @@@@
@@@                 @@@@@                     @@@                        @@@@
@@               @@@@@                        @@@@                         @@@@
@@           @@@@@@                            @@@                           @@@@
@@        @@@@@@                                @@@                            @@@@
@@@      @@@                                    @@@                             @@@@
@@@     @@@@                                     @@@                              @@@@
 @@@     @@@@@                                  @@@                                 @@@@
  @@@@     @@@@@                                @@@                                   @@@@
    @@@@      @@@@                             @@@                                      @@@
     @@@@@      @@@                           @@@                                        @@@@
       @@@@@   @@@                           @@@                                           @@@@
          @@@@@@@                            @@@                                            @@@@
                                             @@@                                              @@@@
                                              @@@                                              @@@@
                                              @@@@                                               @@@
                                                @@@                                               @@
                                                 @@@                                              @@
                                                  @@@@                                           @@@
                                                    @@@                                      @@@@@@
                                                     @@@                              @@@@@@@@@@
                                                      @@@@                        @@@@@@@@
                                                       @@@@                  @@@@@@@
                                                         @@@              @@@@@@
                                                          @@@            @@@
                                                           @@@           @@@
                                                            @@@@         @@@
                                                              @@@@@@@@@@@@@
                                                                @@@@@@@@
""",

    "spa": """
                                                                       @@@@@@@@@   @@@@@@
                                                                   @@@@@@@    @@@@@@@@@@@@@
                                                              @@@@@@@@                   @@@@
                                                         @@@@@@@@@                         @@@@
                                                     @@@@@@@                                @@@@
                                                @@@@@@@@                               @@@    @@@@
                                            @@@@@@@@                               @@@@@@@@@   @@@@
                                       @@@@@@@                                @@@@@@@@    @@@@   @@@
                                    @@@@@@@                             @@@@@@@@@@         @@@@  @@@
                                  @@@@@                            @@@@@@@@@@                @@@@@@@
                                @@@@                            @@@@@
                             @@@@@                             @@@
                           @@@@@                               @@@
                     @@@@@@@@                                  @@@
                   @@@@@@                                      @@@
                  @@@@                                          @@@
                 @@@                                             @@@@@@
                @@@                                                @@@@@@@@@
              @@@@                                                        @@@@@@@@
            @@@@                                @@@@@@@@                       @@@@@@@@
          @@@@                               @@@@@@@@@@@@@@@@                       @@@@
        @@@@                             @@@@@@           @@@@@@                     @@@
      @@@@@            @@@          @@@@@@@@                  @@@@@                  @@@
     @@@@           @@@@@@@ @@@@@@@@@@@@                        @@@@                @@@
    @@@           @@@@@ @@@@@@@@                                  @@@@              @@@@
   @@@@        @@@@@                                               @@@@              @@@@@@
  @@@        @@@@@                                                   @@@                @@@@@@@
 @@@      @@@@@                                                       @@@@                  @@@@@@
 @@@   @@@@@                                                           @@@@                    @@@@
@@@  @@@@@                                                               @@@@                  @@@
@@@@@@@                                                                    @@@@               @@@@
@@@@                                                                         @@@@@           @@@
                                                                               @@@@@@@      @@@
                                                                                   @@@@@@@@@@@
""",

    "hungaroring": """
                  ...:#@%##*+**#%%@@@@*+=:....
                 ...+%-.................:+%=..
  .              ..:#=..    .          ...+=....
         .     . ...*#:...        .    ...-#%-....
                  ...*%-.....            ....*%+:.... .....:-=-:...
                   ....*%*:....             ...=%#-.....-*%#-:=%#:...
                      ...-##=....              ..:*%*=#%*-.....:*#:..
 .     .                ...:+%+:...             .....:.....   ...+#:..
                          ....-#%:..   .            ..         ...+#:..
.                           ....#*..     .                      ...+%:..
        .                     ..**..                . .     .     ..=@=.....
                              ..#*..                  .           ...:*%+-.......
.       .            .        ..**..          .          .        . ...:=+%%**=.....
                              ..=*...  .                  ..          ......:-=*%#-..
      .                       ..-%=.. .   .       .                         .....-%=..
   .     .   ..       .   .    .:#+..              .      .        .   .  .     ..+%:...
      .      .     .           ..=#:..        .   .                             ..-%:..
..                             ..-%=..            .                      .      ..=@:..
      .                        ...++:.    .            . .                   .  ..+@..
                                ..=@-.                                    .     ..+#..
                .               ..:*=..                                      .  ..*#..
                           .    ...*@:.             .             .             ..**..
 .  .                   .        ..-#:..                    .                   ..*+..
               .                 ...#*..       .                               ..:#=..
 .                                ..=%..            .                         ...:#=..
                                  ...%-..                   .                  ..-%-..
                           .       ..#@...               .                     ..=%-..
   .      . .               .      ...%*......                        .        ..=%-.
.             .   .              .  ...*##+-:....                           .  ..+%:.
                    .     .           ....-+*%*=:..    .      ...................+#:..
                      .                 ......:+%+..          ..=*%@%%@@%#*+++=--#+..
    .                                        ...-#:..        ..=#:.........:-====-...
.    .                   .......................**...        ...+%############+....
                    ......-+***##****###*****##%+:..         ...::........:=%+...
                 ....:*%@*=-::::::::::::::::::.....           .....::........:=%+...
       .        ..:+%*-.........................                ...............-%=...
              ..:#%=.....                                   .          .     ..-%+...
 .           ..:@=............................................................:*#:..
             ...*%#**###################################%%%%%%%%%%%%%%%%%%%%%@%=...
""",

    "zandvoort": """
                     .. ..:*%%%#=...
               .      ...-%=...:**..
.                  .....:%+.....-#:..
                    ....=#:.....**...
        .           ....@+.....:%=..
                .  ....##......%#...
            .    .....-@:.....=%:...
                 .....%*.....:@+....
      ..         ....+%......*%.....
             . .....-#-.....:%:.....
 .            ......*#......+%......
           .   ....=%-......*%....
              ....:*+.......+%......                          ....................
              ....=#-.......-%......                          ...............................
             ....:#=... ....-%..                        .    .......:+******###%%%%##**+-....
 .           ....+*:........*#..                  .  .  ..  .....=*%+=-:..............:-+#*.....
.            ...-%=......:*%*:...      ....             ......:*%*:............   .  .....+%=....
            ....#*....+#%#-:................................+#%-:..........................:@+....
          .....=%:.-#%-:...........:+#%%%%%%#+-.........:*%%-:...................        ...=%:.....
         .....:@+..*+:........+%%@*-:::::::::::-=#@@@@@*-:........:-=+***##**+-.......    ..-%-.....
          ....#%...+%:...:*%@*.:........................:*@%%@@#=-............:*%=...   ....+%......
        .....=%.....:%@@@=......       ...........:#@%@*:.......................=%=.........@+..
        .....#*.. .............         ......=@@@=............           .  ...:*=.......:%*....
       .....+#:...   ............ ........+%@#.....                ....... ....:+#:......-#+..
       ....:#=..    ......::-::.......:#%#-........                .........::*%+.......-#=......
      .....+#:....   ....*%=:-%%:.:-#%#.....                  ........::=#%%%*.........-%=...
      ....-#-....    ...-%-....+%@%+........             .  ......:=%##+:.............:%=....
      ...:**...      ...:%+...........               .      ....-##-...........  .....%+.....
      ...=%-...      ....+*..........           .             .-%+.............  ....##.....
      ...#+....      ....-%=.......     .                   ...:*#:............  ...=@:....
   .....*#.....      ....:++....                              ...=%*=..............-%=....
   ....-@-.....      .....=%-...         .                    .....-+%#+-:........-#*....
   ....%*......      .....:*+..                                .......:-++*%@%%%%#+=......
......=%...             ...+%:......                           ..   ..................
......#*...             ...:#=.....
.....:%-... .          .....+%.....
.....:%-...              ...:%=.....
 .....%*.......         .....*%.....
   ...-%-......         .....:@-....
   ....=@=.....           ....@*....
     ...:%*.....        .....:@-....
       ...-%%=.............-#%-.....
       ......-*%%%%%%%%%%%#=:.....
""",

    "monza": """
..:-+#@@%%#*+=+%#.
-%#+-.         .#%:.
@*              .+%=.
*%.              .=%+.
.%*..  .          .-%*.
.-%=.               :#%..
 .+%-           ..  ..+@=.
  .*#:                 -@*:.
   :#+.   .    .        .+%=.
   .=%:.        .        .:#%-.
    .*@%-                  .:%%:
      .%#  .                 .:@%:
 .     +@.                     .-@#:.
       -@=                .      .+@#.
        @*                         .*@#    .
        +%.                    .     .*@#.
        -@-        .              .    .*@+.
       ..%*                             .:*@=.
        .+#.                       .       .*@*@@@*-..
        .-@=     .                           .....:*@=-----------:::::::::.................
         :#+.                                   .   .-*******************#################%%%%%%%*:.
  .      .=%-                    .      . .                              .                     ..+@=
         .:**..                   .                                                               *%
           :##.                         .                      .      .               .        . :%*
            .*%=                             .   .               .   .    .                     :#%:
             .:*%*-.               .--                  .                 .   .    .    .   .:+#%+..
            .   .-*%%#**+++++++*#%@#+@**+++++++++++++++++++++++++++========-----::-=+**##%@@#+-:.
                   ...:---------:....:--------------------------------==============--::....
""",

    "baku": """
. .     .:+*##******###****+:                              .=*****++===--:::...
.     .:*#-.             ..-@.                        . .. =*: ...::----===++***#####**++=-::...
    .:*#-.     .     .     :@+.              ..  .   .    . .++.   .      . .  .     ....:---==+*##-
   .+%-.    ..             ..=%+         .       .      .   -#+.    .     ..          .          .=@
  .*#..         .            .-#    .              . .      =#: .          .     ...      . .     +%
  *#.   .       .            .**  .  .       .#%%%%%%%%%%%%%%+.              .                    +#
 +%.              .     ..  .:%:.  . .   ...:*@:    .     . . .....   .     .                 ..  **
=@.                         .-#.:+%@@@@@%+::-+**+-.     ..              .            ..         . #+
%=.              .   .      ..:=*@@@@@@#=:...........:=+#%@@@@@@@@%*+-:........... ..       .    .@=
.%*.                     . .-@*..   .      .    .        .         ......:-+*%%%%%%%%%#+=:::::...=@.
 .*#.   .  .   . ..     . .+%: ..         ..         .   ..   .   . ..      .         ....::-=+*##:.
...=%-  .   .  .  ..::-=*#%=   .     .      . . .                                 ..    .        .
   .-%=.   ...:-*###*=-...  .     .  .     .       .   .      .   .    .                     .    .
    .:#*. .:=##=..    .   . .                 . .      .      .      .    .  .           ...       .
      .=#*#*=.    .    ....    . .      ..           . .       .          .       .    .         .
""",

    "singapore": """
                                                                                   @@@@@@
                                                                                   @@  @@@@
                                                                                   @@   @@@@@@@
                                                                                   @@         @@
                                                                                   @@         @@
                                                                                   @@@        @@@
                                                                                   @@@        @@@
                                 @@@@@                                              @@@        @@
                                @@@@@@@@@                                            @@        @@
              @@@@@            @@@    @@@@@@                                         @@@       @@
             @@@@@@@@         @@@        @@@@@                                        @@       @@@
           @@@     @@@@      @@@            @@@@@                                     @@@      @@@
          @@@        @@@@   @@@                @@@@@@                                 @@@       @@
         @@@           @@@@@@@                    @@@@@@@                             @@@       @@
        @@@              @@@@                        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@        @@@
       @@@               @@@@@@                               @@@@@@@@@@@@@@@@@@@@@@@@@         @@@
      @@@                @@ @@@@@                                                                @@
     @@@                @@@   @@@@                                                               @@
    @@@                 @@      @@@@@                                                            @@@
   @@@                 @@@        @@@@@                                                          @@@
""",

    "cota": """
                  ...-+#***********************************##%%@@@@@#+-...
                 .-%@@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#######%@@@%-.
               .:%@@+..            .             .  .                 .=@@#.
             ..#@@*.         .                            .            .-@@+
           ..+@@%:..                         .     .                   .-@@+
.     .  .=%@%-.                   ..                                .:%@#.
    ..........-%@@+.  .         .                                       ...+@@#..
  ..=#@@@@@@@@@%+.        .    .       .       .        ..            ..=#@@%-.
 .=@@@+-:::::...    .   . .                        ..-=*#%%+.       .-#@@@+...
.-@@+.  ..  .      .   .         .      ....:=*%@@@@@@@@@%@@@: . .:*@@@#:...
.*@%..                               ..=#@@@@@%#*+=:......:%@* .:#@@#-...
.@@-                                .-%@@+:......        .#@%..-@@*...
+@%.        .                      ..#@%..     .       ..#@%...#@#.
.@@+.      .                      .  .%@+      .       ..#@%-...#@#..
.=@@-        .             .    . .   .%@=              .*@@-.  .-@@@#*+++++++++++**+=:
.#@#.              .    .        .    :@@-            ..*@@:.     .-#%@@@@@@@@@@@@@@@@@@=.
:@@+.     .                          .:@@.           ..*@@-.     .  ....   ...... ....+@@-.
-@@=..              .         .       -@@.           .+@@=.                      .  ..-@@=
..#@@@@@%%#**+==-:::::.......     .....*@%.          ..#@#..  ..   .  ........::::::--*@@%.
  ..-=+***##%%@@@@@@@@@@@@@@@@@%%%###*%@@-.          ..*@@#*####%%%@@@@@@@@@@@@@@@@@@@%*-.
.       .    .     ..........:::-=++*##%@@%+..    .       ..-#@@@%%#**++=--:::.............
""",

    "mexico": """
                                                                     .  .
                         .                .                                               .    .
                              .   .      .          .                                .          .
     .       .                  ..::...   .        .   .        . .  ..      .             .      .
          .                   .:@@@@@@#.     .    .  .            .    .
.                            .=@@*:.:#@@-     .                      ...-=+******++=:..
          .                  .*@%..  .#@#.                  .       .:#@@@@@@@@@@@@@@%:.
           ...-*%%+..   .    :%@+     +@%-.       .          .     .:@@%...       ..#@%:.
       ..-#@@@@%#%@@#.       -@@-    ..@@#.                       .:@@+.   .       ..%@%:
  .   .:@@@*-:.....#@@.      +@@.     ..@@*.                     ..%@#..            ..#@@:
 .     @@*.        :%@#.  .  #@#.       :%@@:..               .  .*@@-.     .   .     .*@@-.
      .%@*.         =@@-.   .@@=.    .  ..*@@%-..               .-@@=.    ..          ..#@%-.
  .  ..:@@-        ..%@#.  .-@@:.          .+@@%:.    .        ..%@*.              .   ..%@*.
  .    .*@@..       ..@@=.  +@%:         .  ..%@%:             .#@%.                  ..=@@+.
       .-%@*.     .   +@@. .%@*.  .          .=@@:            .*@%-.                ..:#@@+.
       ..+@@-.        :%@*.:@@+.             .@@*.           .=@@=.               . .+@@#..
 .      ..@@#.        .=@@**@@-.            .+@@-       .  ..=@@+.            .   .:#@@=.
         .-@@-.     .  .-#@@%=..            :%@*.    . . ..:%@@-  .             ..+@@#..
           *@@..  ..     ....    .         .+@@:        ..#@@#..               .-%@%-.
         . :%@*.                .          .%@*    ....-%@@%...              ..*@@#..
.          .=@@-.  .            .   .      .%@+.. .-+%@@@*:..         .     .-@@%:.
 .         ..#@#:                          .=@@@@@@@@%=:..  .      .     . .:%@#..
            .:@@+..    .         .       .   .:==-..   .                  ..:%@+..
              -@@*:..  .      .           ..                               ..+@@+.
              .:#@@@#:                                    .     .            .-@@*.
         .      ..:#@@@%=....                                      .          .-%@%..
   .        .      ..:+%@@@+..     .         .             .       .           .:%@#:.
""",

    "interlagos": """
              .+#***+=-...
         ..:+%@@@@@@@@@@@@#=...
       ....-+#@@@@@@@@%#+=--::.:-=#@@@%+...
                           .       .  :+@@@%=...
                                      ..:#@@@%=...
                                         .*@@@%.....
                                          .#@@-...
                                          .*@@:.
                                           :@@%-.
                                            .*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*-.
  .     .   .  ...::::::::----------------------------------------------::::::::::::::::::...
""",

    "las_vegas": """
                    @@@@@  @@@@@@@@                                            @@@@
                    @@  @@@@@     @@@                                         @@  @@@#*
                    @@             @@@                                        @@    %=**
                    @@              @@@                                        @@    @@@@@
                    @@               @@                                         @@@      @@@
                    @@               @@                                           @@       @@@
                    @@               @@                                           @@         @@
                   @@@               @@                                          @@@          @@@
                   @@                @@     @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@             @@
                   @@                 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@                            @@
                   @@                                                                          @@
                   @@                                                                          @@
                 @@@                                                                           @@
               @@@                                                                             @@
           @@@@@                                                                               @@
       @@@@@                                                                                   @@
     @@@                                                                                       @@
    @@@                                                                                        @@
   @@@                                                                                         @@
   @@                                                                                          @@
   @@                                                                                          @@
   @@@@                                                                                        @@
      @@@@                                                                                     @@
         @@@@                                                                                  @@
            @@@@@                                                                              @@
                @@@@                                                                           @@
                    @@@@@                                                                      @@
                        @@@@@@@                                                               @@@
                             @@@@@@@@                                                        @@
                                    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
""",

    "qatar": """
                         .                .
                              .   .      .          .
     .       .                  ..::...   .        .   .        . .  ..
          .                   .:@@@@@@#.
.                            .=@@*:.:#@@-                           ...-=+******++=:..
          .                  .*@%..  .#@#.                  .       .:#@@@@@@@@@@@@@@%:.
           ...-*%%+..   .    :%@+     +@%-.       .          .     .:@@%...       ..#@%:.
       ..-#@@@@%#%@@#.       -@@-    ..@@#.                       .:@@+.   .       ..%@%:
  .   .:@@@*-:.....#@@.      +@@.     ..@@*.                     ..%@#..            ..#@@:
 .     @@*.        :%@#.  .  #@#.       :%@@:..               .  .*@@-.     .   .     .*@@-.
      .%@*.         =@@-.   .@@=.    .  ..*@@%-..               .-@@=.    ..          ..#@%-.
  .  ..:@@-        ..%@#.  .-@@:.          .+@@%:.    .        ..%@*.              .   ..%@*.
  .    .*@@..       ..@@=.  +@%:         .  ..%@%:             .#@%.                  ..=@@+.
       .-%@*.     .   +@@. .%@*.  .          .=@@:            .*@%-.                ..:#@@+.
       ..+@@-.        :%@*.:@@+.             .@@*.           .=@@=.               . .+@@#..
 .      ..@@#.        .=@@**@@-.            .+@@-       .  ..=@@+.            .   .:#@@=.
         .-@@-.     .  .-#@@%=..            :%@*.    . . ..:%@@-  .             ..+@@#..
           *@@..  ..     ....    .         .+@@:        ..#@@#..               .-%@%-.
         . :%@*.                .          .%@*    ....-%@@%...              ..*@@#..
.          .=@@-.  .            .   .      .%@+.. .-+%@@@*:..         .     .-@@%:.
 .         ..#@#:                          .=@@@@@@@@%=:..
            .:@@+..    .         .       .   .:==-..   .                  ..:%@+..
              -@@*:..  .      .           ..                               ..+@@+.
              .:#@@@#:                                    .     .            .-@@*.
         .      ..:#@@@%=....
   .        .      ..:+%@@@+..
""",

    "abu_dhabi": """
                                                                                          ..-=*#%@#:
                                                  .                                 ..:-=*%@%#*=:+@%
                                                   .         .   .              .:-=#@@%#*-::-=*@@%-
                   .                                                 .     ..:=#@@@%*-. .-*@@@%*-.
                                               . .                   ...:=#@@@%*-..    .-@%-.
                                                                 ..:-*@@@%*-.           :#@=.
                         .                                 ....=#@@@@*-.   .     .     .:#@+.
                      .                .                 .-#@@@@#-.   .               .+@%=
         .                       .                 ..=#@@@@*:....                  ..-@@*..
.             .                                .=%@@@@*-...                    .   :%@#:..
     .      .                            ..=#%@@%*::..                           .#@%:..
                                    ..-*%@@%*-:..      .         .             .*@@-.
                                .-*#%@@*=:.                                  .+@@+.
                       .   ..=*%@@%=-:              .                     .-*@@+..
                      ..-+#@@%*=:      .    .                         ..-*%@#=..
         .        .:=*%@@#+-...                                    .-*#@@*=:.
            ..:=+#@@%*+:.            . .                        .=#@@#+-.
       ..:-+#@@%#*: .         .             . .     .         .-%@*-
.    .:*@@%#*:.     .                             .  .       .+@%:.
    .-@@=.       .:-:.              .        .            .. =%%:.     .   .
     .=@%=.    .-@@@@@+..                                   .#@-.
       :#@-.  .=@@ ..+@@+..                              .  .#@-.
      .=@%-   :@@.  . .+@@+.                               ..#@-.
     .*@#:.  .%@-      ..+@@=.                               +@%:.
   .:%@+.   .#@+.        ..*@@+.                           . .*@=.
  .-@%=.    =@%.           ..*@@+.     .                      .%@:.
 .-@%-  .  -%@:.   .       .  .+@@*.           .               +@#.
 :@%:     .#@=.                 .+@@+.                    .    =@%.
.%@=      .#@+.                   .+@@+.   .                 .=@@:.
=@#        .+@@+.                  ..*@%=.  .               .*@#:.
*@+     .    :*@@=.                  .:*@%=...             -%@*.
%@-            :*@@=.                  .:*@%=.           .+@%-.
@@-              .#@%-.                   :*@@+.    .   :*@*:
@@:               .:#@%-.            .      :*@@=.    .=@%=..
@@:                 .:#@#-.                   .*@@-...*@#:
@@:             .     .-%@+.      .     .       .#@@@@@*.
@@:       .             :*@=.          .   .       ...
@@:  .     .....  .      -#%-
@@:       +@@@@*.      .-%@+.
@@-     :#@*:.=@@*   .-@@*:.
%@-   .=@%=.  ..=@@#+@@*:.
%@- ..+@#:.      .-#@=..
#@-  -%#:         ...
#@=  -@#:          ..
#@= .:%%-
*@+  :#%-
*@+ ..*@=
=@*  .=@+.
:@%.  :#%=.
.@@:   :*@%=.
 *@+     :*@%=..
 :@%.      :#@@-.
 .#@=        .#@@-.
 .=@#.         .#@@=
 ..%%-          ..#@%=
. .=@*            .:*@%=
  .:%%-             .:*@+.
   .+@+..            .-@#:
   .-%#-           .-#@#:.
    .+@+.         =%@#-.
    .-%%==*%@%*-=%@*-.
     .-#%%*-:=#@%*:
""",

    # ── GT3 / Shared Tracks ────────────────────────────────────────────────
    "paul_ricard": """
                                                                                @@@@@@@@@@@@
                                                                          @@@@@@@@@@      @@@@
                                                                    @@@@@@@@@          @@@@@@@@@
                                                     @@@@@@@@@@@@@@@@@                @@@ @@@ @@@
                                                     @@ @@@@@@@                     @@@@   @@   @@@
                                                @@@@@@                          @@@@@@     @@    @@@
                                          @@@@@@@@@                     @@@@@@@@@@@@       @@     @@
                                   @@@@@@@@@@                          @@@                  @@   @@@
                            @@@@@@@@@@                                 @@@                  @@@@@@@
                     @@@@@@@@@@@                                        @@@
 @@@@@@@@      @@@@@@@@@        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@  @@@@@@@@@@@@@               @@
@@ @@@@@@       @@@@@@@@@@@@@@@@@
 @@@@  @@@@@@@@@@@@@@  @@@@@@@
""",

    "donington": """
                                                                    ..*@@@@#=:.
                                                                    =@%.   :%@@@=.
                                                                  .+@*.      .=#@@#=.
                                                                 .=@#.           .=%@@*:..
                                                               .*@*.    ..          .:+@@-
                                                           ..-%@%-    .       .        :%%
          .   .     .=##+:..      .   .-#%@%-.                       :@#    .
                  .+@%**##%@@@@*=--+%@@%*.                            .*@-.
                 .@@-.   .....:-=++--.                            . .=@@=.
              ..+@#:                                           .-#@%+
    .     .  . #@+.                                       . .=@@@=...
           ...:@@=                                      .-*@@#=
          ..#@@#.                                    .*@@@+..
    .=*@@@%+:.                   .               .=#@@*-.
    .@@@+.  .               .              .  .+@@@=.
   :%@+..                                   =#@@*-.
  .=@#.             .                  ..-@@@+.          .
   -@#.        .              ..=**=.   -@@#-.
   %@.                    .:+@@@%+*@+.  -@#
  :@*              .   .=#@@@+-...+@@=..+@@+.
  *@-           .:=@@@%+.   .:%@%-.+@@#:
  .@%:      .-#@@@*-..    .+@@+.=%@#:.
  .@%:     .:=%@@%*:.       .+@%=:#@%=.
   -@%-.=#@@@*:.... .      .#@%:+@@+...
    .+##*+:.            :%@#-#@%=.
                       :%@*:%@#..
                       :%@+%@+.
                        :@@=
""",

    "oulton_park": """
                                                                    .  .:=%@@@@@@#-.
                                              . .-+**=-:..       .. .  -#@@@+:.. .:*@@=
                                      ..      .=@@###%%@@@@@@@*+=-==+*%@@@#=.    .   #@+.
.                                             :@@.        .::-=*%%%%*=-:::..               :%@-
. . .     .         ..            ..::@@-      .                            . .     =@#.
      .             .  .         =@@@@@+.   .  .                           .        .#@+
                              .-@@# .  . .      .  .                     . .         .%@=.
                          .  .#@@:         .      .                .                  :@@-
             .    . .      .=@@=       .                    .     .          .  .      -@%:
 .   .             .      :%@#.     .=#%%#:.                 .                        . -@%.
                        :#@%:    ..*@@#++#@@.                      .              .     .=@%.
.                .   .:#@@:     .#@@=.....+@%.                 .      .                  .*@*.
                   .:%@%-   . :%@%-       .#@*.                                           .#@+
.       .         :%@%:.    :%@@:  . .   . .@@=   .     .          .         .       .     .#@=.
                .*@%:    .-%@%-             .%@#.. . .        ..                            :%@-
               :@@*.    -@@#:        .   .   .+@@:       .           .                       *@*.
.           +@@@@+   .=@@#.               . .  :%@#.                      .      .......::--#@%:
    .       %@:..  .#@@+..               .      .+@@:.   ..             .   .=#%@@@@@@@@@@@@*:.
. .       .+@#. .:*@@+..     .                    .%@%:.               .-*@@@%#-...    .
         .+@%. .*@%-.                           .  .-@@#.           =#@@@*-..
       . :@@. .%@+                              .    .=@@-.    .:*@@@#:.
         *@=  =@*.                      .  .           .%@%#*#%@@%-..
         %@:  =@*. ...             . .                   .=###+:.
    .    *@=  :@%. ..                            .           .
         -@#   +@#.     .   .               .  .
         :%@:  .#@*.      . .
         .*@*   .@@=.   .         .
          -@%:   :@%. .           .
           =@@-..=@%.     .            .
            :#@@@@#..            .
""",

    "snetterton": """
                                               .:=+#%@@%+.
                            .         .  .     .-=#%%@@%*=-:..:*@#.
                    ..            .            =@@@@%+:.            .%@=.
                  .          .         .      ..+@=                    .=@+.
.        .                                  .   .*@:              .      .-%#.
                                              .                    .             :%@:
                        .          .       .   .*@: .      .       .       .#%-
    .                                     .   .-@=.                 .       .#%:
.      .  .                     .             .+@+.            .      .       :%*.
           .             . .                .=@@=..                          ..+@-
                                         .*@#-.                        .      :%*
                                      .*@*.         .  .   . .         .       .##
                     .                *@*.                              .       .##
                   .                 +@@-.                              .      -%*
                                   .*@@:                              ..    .*@=.
                                  .*@%.                            .        .-%@+.
                ..   ..:..... ..+@@%:. :@@.
     .           .-%@@@@%*=:+@@#:.   =@@
                 #@@+..-#@@@@@..    .@@=
.               -@@*=--::..      .-+@@%:
                .-%@@@@@@@@@@@@@@@@@#:..
""",

    "hockenheim": """
  .        ..             . .       .-=*#%@@@@@@#:.
                        ......-*%@@@@@@@@@%+-.#@@-
                  ..-+*#%@@@@@@@%#+=-:.      :@@%:
               .:%@@@@@@%*=:....            -@@%.
       .      .*@@#-              ...  .    -@@.
              =@@+.                         -@@#.
              *@%           .           .   .+@@*.
   .         .@@*.      .                  . .=@@%.
..           -@@:   .                         .:@@@:.
          .  +@@.                         .    ..#@@-
             %@#.                              . .+@@:
.           .@@=.       .          ..             .+@@+.
.    .      -@@-    ..-=:..               .        .=@@#.
.       .  .+@%:  .:@@@@@@:    .                   . .@@@-.
           .#@*.  :%@%:.%@@.                      .   .#@@%:
.         .:%@+  .+@@=  =@@-.                  ..      ..@@@@:.
          .=@@:  .*@@.  -@@*               .          .   :#@@@+:.
          .+@@. ..+@@+. :%@*                     .     ..+*+:-%@@@@+.
          .#@#    .=@@%..#@*                           .*@@@@@@+.-*@@@@%+-..
    .     :@@-      :@@+.#@#                          -@@-..=@@@+. .:+@@@@@%#=..
          -@@..     :@@#.*@%.         . .         .   +@@.. ..+@@@-.    .-#@@@@@@%+:....
  .       -@@:.     -@@+ -@@+.                    .   @@@.      =@@@=.      ..-=*%@@@@#=..
.         .*@@@%**%@@@@.  +@@%:..  .               .:+@@+   .    .=@@@+..           .*@@#..
.          .:+#%%@%%#+.    .*@@@@@@@@@@@@@@@@@@@@@@@@@@*.          .=%@@@@@@@@@@@@@@@@@@+.
                             ...::-=====--::::..........     .        .:=*####***++==-:..
""",

    "oschersleben": """
                              ...::-=+###%%%%%@@@@%%%#*+==#@=.
       ...::--===++*#@@@@@@%%##***+=-:.                .   .%%:
     .*@@%+=-:::......              .        .              .=@+.     ..    ...:-=#%%@@@+
   .*@-..             ......:-==+++*#%@@@@@#***%@=            .+@@#%%@@@@%#**+++=:..   .#@:.
   *%   .      .-@@@@@@@@@%%+-..                .#%.                  . .     .. ..      -@-
   #*      . .*@+..                              :@-          . .    .                   .:@*.
   -@:     .:@*.        .          .  .    .....:%#.  .     ..      ..                      %#.
   :%+     =@- .             .   ....-+**##@@@@@+:              .                           .+@-
. .*%     -@-          .:::-*@@@@%%%%=.                                      .             .  -@+
  *%:    .@#.        *@@=--:...                 .         .  .                   ..     .  .   :%+
 .+%:     ##.      :%*..          .    .       .                .          .              .    :%*
  .#*   ..-@:  .   +%     .  .+@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@=.
   :@=    .@-      =@.     ..##.
   .+@-    +@.     .#@###%%%@*.
    .##.   .:*@-     ........
     .@=     .*#
     .=@:    :@-
      .*@+-+%@=..
        .:::..
""",

    "imola": """
                     .     .                    .                    .
                                                               . ..    .
       .           .               .        ...
     ..                                                         .
.                                         .          .   .
.                     .     .                    .                           . .     .......
                     .                                         .                  ......:-:..
       .                           .       ...... .                          ......:=+%#**%=..
                            .  ............................      ..............:=*%*+:....-%=..
      .                    ......:-+++**#%@%%##%@%#*++=-:.................:=+*%*=:.........=@:..
                     .   ...=*#@*+==-:..............:===+#%%%%@@@@@@%%##**+=-...... ....:+*%+...
                       ....=%-.........      .     ...........................   ....-*#*=:.....
                   .  ....=%+... .             .                                ...+%+-.....
         .     .    ...+#%+:...   .    .                                    . ...=%+....
             .     ..+%-:....                      .                         ..:#*:...
                  ..-%-...                                   .       .     ...##-....
                 ...**..     .              .          .              .  ...*%=....
 .    .         ...+%:..                 .                            ....*@=....
                ..-#-..   .         ..                       .     ....=@%=...
 .              .:*+...            ................................-%@@-....
        .      ..=%-..            ...:@*#@%%%%%%%@@@@@@@%##*+=*@%%%-.....
              ..:@+..            ...=%:...............................
            ....*#...            ..:#:..           .
            ...-%:..             ...#+..
   .        ..:@+..    .          ..+%..
            ..:@-..      .  .     ...%+..
     .       ..##..        .       ..*@..
           ...:*#..                ...@-..
   .     ...:*#=...                ...@+..
        ..:*#=...      .           ..-@...
     ...:*#=...  .    ........    ...%*..
    ...*%-............:-===-:.......*#...
 .  ..+%...:=+**#%@%#+===--==+*%@%%%+...
    ...=##+=--::......................
""",

    "watkins_glen": """
  .                           ...-+#***********************************##%%@@@@@#+-...
                 .           .-%@@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#######%@@@%-.
                   .       .:%@@+..            .             .  .                 .=@@#.
                         ..#@@*.         .                            .            .-@@+
                       ..+@@%:..                         .     .                   .-@@+
.     .      ..       .=%@%-.                   ..                                .:%@#.
           ..........-%@@+.  .         .                                       ...+@@#..
         ..=#@@@@@@@@@%+.        .    .       .       .        ..            ..=#@@%-.
        .=@@@+-:::::...    .   . .                        ..-=*#%%+.       .-#@@@+...
.      .-@@+.  ..  .      .   .         .      ....:=*%@@@@@@@@@%@@@: . .:*@@@#:...
 .     .*@%..                               ..=#@@@@@%#*+=:......:%@* .:#@@#-...
 .     .@@-                                .-%@@+:......        .#@%..-@@*...
      .+@%.        .                      ..#@%..     .       ..#@%...#@#.
  .   .@@+.      .                      .  .%@+      .       ..#@%-...#@#..
     .=@@-        .             .    . .   .%@=              .*@@-.  .-@@@#*+++++++++++**+=:
.    .#@#.              .    .        .    :@@-            ..*@@:.     .-#%@@@@@@@@@@@@@@@@@@=.
     :@@+.     .                          .:@@.           ..*@@-.     .  ....   ...... ....+@@-.
     -@@=..              .         .       -@@.           .+@@=.                      .  ..-@@=
   ...#@@@@@%%#**+==-:::::.......     .....*@%.          ..#@#..  ..   .  ........::::::--*@@%.
      ..-=+***##%%@@@@@@@@@@@@@@@@@%%%###*%@@-.          ..*@@#*####%%%@@@@@@@@@@@@@@@@@@@%*-.
.       .    .     ..........:::-=++*##%@@%+..    .       ..-#@@@%%#**++=--:::.............
""",

    "road_america": """
                    .              .........:-=+****+=-...
            .             ..........:-=+#%@@@@@@@@@@@@@@#=...
                       ....-+*##%@@@@@@@@@%#+=--::.:-=#@@@%+...
                 .   ...+%@@@@@@@%%*+=--:....        ..:+@@@%=...
   ..               ..=%@@@#=-:............       .    ..:+@@@%=...
 .    .           ...=@@@+........                   . ....:*@@@%=..
         .        ..:#@@+... .                      .     ...-#@@@%-....
                  ..:#@@:.          ...........            ....-#@@@%-.....
 .              . ..:#@@-.     .  .....+%@@@%=..              ...-%@@@#-...
            .      ..=@@@:..      ..:+@@@@@@@@*:..      .       ...:#@@@%-..
     .              ..+@@@#.... ..:#@@@%-..:%@@%:.                 ..:*@@@@#:....
                      .:%@@@@%##@@@@@%-......+@@@+..      .         . ..=%@@@@%=.....
   .                   ...*%@@@@@@%*:.........-%@@@:..                .....-#@@@@@#-:......
                     .   ............       ....#@@@*....                .....:+%@@@@@@*=:........
                                           .   ..+@@@%-.. .             .    .....:*%@@@@@@@%*-:....
         . .  .    .          .                 ...%@@@+..                         ....:+#%@@@@@@+..
                                ..               ...*@@@#:.    .                          ..:+#@@@=.
                                   .               ..=%@@@-..        .        .             ..-@@@=.
            .           .       .   .              ...:#@@@*-:::::---===-:..                ..*@@#:.
.....:-==-::..........           .  .            .   ...-#@@@@@@@@@@@@@@@@@-..      . .   ...-@@%-..
..-#@@@@@@@@@@@#*+=-:....     ...                 .    ...:=++++++=====+#@@@..          . ..:%@@+...
.:@@@%#####%%@@@@@@@@@@@@@%#*+=:...  ....          . .      . .         ..:%@@:. .          .:%@@*:..
.+@@#:.  .......::-=+*%@@@@@@@@%#*=:....  .    .                      ...%@@-           ..+@@@#:..
.*@@*..          .   .....:-=+%@@@@@@%#+-.....       .                 ..%@@-.       ...=%@@@=..
.#@@*..                   ......:-=#@@@@@@@#*-......               .  ...#@@-.      ..:*@@@=....
.*@@*..        .                ......-=*@@@@@@@%*-......             ...#@@=..     ..=@@#:...
.+@@#:.           .      .            .....:-+%@@@@@@%+:.......       ...#@@*..     ..*@@+...
.=@@%-.          .                     .    .....-+%@@@@@@%+:....      ..#@@#.      ..*@@+..
.:@@@=..                 .                  .     ....-+%@@@@@@@%*=:.....#@@%..     ..=@@%:.
..#@@*: .       .                          ..           ...:+%@@@@@@@@@@@@@@*..      .:#@@*...
 .+@@%:.                .                             .      ....-+#%@@@@@%-..       ..-%@@-..
 .-%@@-..       .    .            .            .         .     ..............   . .   ..+@@%..
 .:#@@=.            .              .   .                                             ...:#@@=.
 ..+@@+.                                                            . .           .   . .*@@+
 ..=@@*...                                   .                        .    .         ....*@@+.
 ..:#@@=...       .                                    .                             ...-%@@-.
 ...=%@@@*+==-------====++++++++++++++++++++++++=================================----=+#@@@#..
   ..:+#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*..
 . . .....:--=========----------------------------------==================++++++++++++=-:...
""",

    "road_atlanta": """
      .-**=-:...
      *@@@@@@@%#*-..
.    .@@#....+%@@@@@@@@@@%%%%%%%%%%%%%%%%%%%@@@@@@@@@%#*+=:....
     .@@#.       .:-++*####%%%%%%%%%%%###############%%@@@@@@@%#+-.
     .@@#.           .                     .  .. . .... .....=%@@@@@%-.
     .*@@+--:::::....                       .          .   ..   .:+#@@@@%+-..  ..:--..
      .-%@@@@@@@@@@@@@@@%%#+=:.                 .           ..      ..:*@@@@%#-+@@@@@%+..
       ... ......::-=+*%%%@@@@@@@@@#*-..   .                            ..:*%@@@@*..*@@@%-..
 .  .            .       ....:--=*#%@@@+.  ..       .       .               ..::..  ..:+@@@=.
        .                           .=@@-     .                               .         .%@#:
                         . .   .     .*@@=.             .                               .-@@+
           .                         ..#@@#              .         .                     .#@@.
               .                       .:%@@-.  .                                .        :@@+.
        .   .    .  .      .            .:#@#.               . . .     .                  .#@@.
  .      .    .         .          .     .+@@+..            .   .  .                      .*@@.
.            . .            .             .=@@@*-...       .   .                         .-@@*.
  .             .  .       .                .=@@@@@%+..                                ..#@@*.
                  .  .  .                .     .:=*%@@%-.             .   .    .     ..-%@@-.
  .            .              .                    ..*@@*                           ..%@@*..
                    .   .     . . .           ..      =@@:              .   .     ..=@@%-.
         .              .              .              -%@%:.                     .:%@@+..
.       .                       .                     .=@@@@@=.                ..+@@%:.
         .  .       .                     .   .          .-+@@@+.            ..-%@@=.
                            .           .               .   .=@@#:.          .+@@#:
     .                                                  . . ..:@@@=..     ..-%@@=.
        .            ..                     .           .    ...+@@@#:.   =%@@*..
       .      .              .                         .      .  .=%@@@@@@@@*..
                                   ....                            ..-+#*=:..
""",

    "beijing": """
                   .      .            .  .     .        .   .              .     .  .       .
              .                         .            .                                              .
 .                                            .                                      .         .
          .                                          .                 .            .   .
                                            .                 .         .                   .      .
  .                                     .        . .       .                        .    .    .
            .          .           .                               ..       . .   .
     .              .          .                                .        . .              .   .
                                       .                                                         .
  .        ..             . .       .-=*#%@@@@@@#:.
                        ......-*%@@@@@@@@@%+-.#@@-
                  ..-+*#%@@@@@@@%#+=-:.      :@@%:
               .:%@@@@@@%*=:....            -@@%.
       .      .*@@#-
              =@@+.                         -@@#.
              *@%                               .+@@*.
   .         .@@*.                               .=@@%.
..           -@@:                                 .:@@@:.
          .  +@@.                                   ..#@@-
             %@#.                                    . .+@@:
.           .@@=.                                       .+@@+.
.    .      -@@-    ..-=:..                              .=@@#.
.       .  .+@%:  .:@@@@@@:    .                         . .@@@-.
           .#@*.  :%@%:.%@@.                               .#@@%:
.         .:%@+  .+@@=  =@@-.                           ..@@@@:.
          .=@@:  .*@@.  -@@*                          .:#@@@+:.
          .+@@. ..+@@+. :%@*                      ..+*+:-%@@@@+.
          .#@#    .=@@%..#@*                      .*@@@@@@+.-*@@@@%+-..
    .     :@@-      :@@+.#@#                     -@@-..=@@@+. .:+@@@@@%#=..
          -@@..     :@@#.*@%.                    +@@.. ..+@@@-.    .-#@@@@@@%+:....
  .       -@@:.     -@@+ -@@+.                   @@@.      =@@@=.      ..-=*%@@@@#=..
.         .*@@@%**%@@@@.  +@@%:..               .:+@@+   .    .=@@@+..           .*@@#..
.          .:+#%%@%%#+.    .*@@@@@@@@@@@@@@@@@@@@@@@@*.          .=%@@@@@@@@@@@@@@@@@@+.
""",

    # ── GT4 Unique Tracks ─────────────────────────────────────────────────
    "misano": """
                                                       ..-=+=--:..
                                                    -*%@@@@@@@@@@@@@%%*=:.
.                                            ..:+%@@@@#=.. .:==-::=+#%%@@@@@@*-..
          .             .              ..:+#@@@@#=:.     .@@@@@@@@%#*-...:-+@@@*..
.                         .          :*@@@@@*.         ..#@#.    :*%@@@@@*:..:%@@#..
     .         .                .-+#@@@%*=.  .-=++-..  ..#@@.         .:=*%@@@+.:#@@*.
             ...  ..          -%@@@@%=..  .+@@@@@@@@@:  .#@@.   .           .:%@* ..#@@:
  .        .  .  . .     .-+%@@@%*-.  ..-#@@@%+:   .*@@. *@@-                 .+@@.  .#@+
 .        ..            :%@@@#-..    .*@@@@+:.      *@@:.=@@-.               .  =@@-  :@@:
                        -@@*.     .:*@@@%=..       .#@@-.-@@=   .                :%@+. #@#.
     .                  =@@=-:.:=#@@@*-..     . . .%@@:..@@+                  .. .#@#.-@@-.
  .    .               ..=@@@@@@@@=..        .  .:@@#. .@@+.               .     .+@%-@@*.
.          .         .           .      .      .=@@+. :%@%..                      .%@@@%:
.      .                              . .      #@@:.  %@@.                          .....
    .        .                 .          . .:@@%:  .#@%.
                           .                =@@*.  .*@%:.
.       .                              . .:@@@:   .+@@-
    .                     .       .     .*@@*..   -@@:
                       .             ..-@@%. .. .-@@-
.         .           .             .:%@@=. .  .-@@+.
.            .       . .           :%@@=....  .:@@*..
                                 .*@@*:#@@@@@@@@@=
                              ..*@@*..*@%:::::::.
              ..   ..:..... ..+@@%:. :@@.
     .           .-%@@@@%*=:+@@#:.   =@@
                 #@@+..-#@@@@@..    .@@=
.               -@@*=--::..      .-+@@%:
                .-%@@@@@@@@@@@@@@@@@#:..
""",

    "nurburgring": """
                                                                .
                                  .=#*:     .  .-++=*@@@*
  .                             .-%@#%@%---:.*@@%%#%#*+@#
                              :#@@@= .+@@@@@@@@: .    #@-
                   .          :%@%=.        ..   .   .%@-
            .                  .=%@+         .        -%@*:.
.           .              .    .#@+  .    . .        ..+@@@%#*-.                .--.
 .                 .         .=@@@=.  .   .               .:=#@@@@=.    -*#%@+. =@@@@@*.
                          .-#@@#:.         .                    :#@%=-#@@%@@@@+.+@@.:*@%+.
                         .:%@+..                                 .:#@@%-+@@%*+*#@@-  .:*@%.
              .   .     ..%@+.   .               .                   .  +@@@@@@*=.    .=@@:
        .               .*@*.                    .       .           .   .:.   .      :#@+.
           .      . . :*@@*.                          .                        .      .:#@#.
      .     .  ....=#@@@+.   .                  .                                  .-@@@@@*.
    .          :%@@%*=.                .  .                  .                    .*@@=-=-.
               .+@@#:     .                                                       -@#.
.  .              =@#. .          .  .   .                                    ....*@+.
                  .#@-                     .  .                    .         .-%@@@*:
                  .=@%.                   .                        :-:.     :#@%-..
            .      :%@-         .                              . =@@@@%*#%@@@@+..
                   -%@:         .               .. .             -@@#****+=-..
                  .+@%.   .   .                                   .:#@*
       .         .-@@:                     .               .     ...=@%
                  @@- .      .                            .. .:=*%@@%+:
                 .+@%.                  .                .:*%@@@%=:..
                  .+@@-.   .                       ..:=#@@@%*:.
      .  .         .=@@*.              .       ..-*%@@@*=:.
   .                 .=@@..                 .=%@@@%=:..
        .             .*@@@-.     ....    .+@@#-.
  .    .                 -@@##*=:+@@@*. .-@@*.
.            .    .      .:#@+#@@@#%@#::%@@-.
     .         .     .  .:+%@@@@@@@%##@@@=..
                      .=%@@+------+%@@+:..
                      :@@+.    .*@@%:.
         .             -@@=+@@@@@+.
              . .     :#@*+@@++:.
       .  .           #@+*@#..
     .             ..=@@:=@@*
.      ..         .=@@*+%@@#:
          .      ..=@@@@%:..
        .  .   .    .:-.
""",

    # Shared: barcelona (GT3/GT4 use same map as F1 'barcelona')
    # Shared: spa (GT3/GT4 use same map as F1 'spa')
    # Shared: zandvoort (GT3/GT4 use same map as F1 'zandvoort')
    # Shared: red_bull_ring (GT3 uses same map as F1 'red_bull_ring')
    # Shared: suzuka (GT3 uses same map as F1 'suzuka')
    # Shared: donington, oulton_park, snetterton, watkins_glen, road_america for GT4

    "default": """
  ╭─────────────────────────╮
  │      Track Layout       │
  │   ASCII map coming soon │
  │                         │
  ╰─────────────────────────╯
    """
}

# Alias maps for tracks that share layouts across categories
ASCII_MAPS["spa_gt3"] = ASCII_MAPS["spa"]
ASCII_MAPS["spa_gt4"] = ASCII_MAPS["spa"]
ASCII_MAPS["suzuka_gt3"] = ASCII_MAPS["suzuka"]
ASCII_MAPS["red_bull_ring_gt3"] = ASCII_MAPS["red_bull_ring"]
ASCII_MAPS["barcelona_gt3"] = ASCII_MAPS["barcelona"]
ASCII_MAPS["barcelona_gt4"] = ASCII_MAPS["barcelona"]
ASCII_MAPS["donington_gt4"] = ASCII_MAPS["donington"]
ASCII_MAPS["oulton_park_gt4"] = ASCII_MAPS["oulton_park"]
ASCII_MAPS["snetterton_gt4"] = ASCII_MAPS["snetterton"]
ASCII_MAPS["watkins_glen_gt4"] = ASCII_MAPS["watkins_glen"]
ASCII_MAPS["road_america_gt4"] = ASCII_MAPS["road_america"]
ASCII_MAPS["paul_ricard_gt4"] = ASCII_MAPS["paul_ricard"]
ASCII_MAPS["zandvoort_gt4"] = ASCII_MAPS["zandvoort"]
