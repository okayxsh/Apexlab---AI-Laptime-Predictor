"""
Run this once locally to generate all predictions from the real ML model.
Output: src/predictions.json (import this into the frontend)

Usage:
  cd laptime-predictor
  python generate_predictions.py
"""

import json
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "model"))

from predictor import predict_lap_time
from data import TRACKS, CARS

results = {}

# ── Circuit categories (F1, GT3, GT4) ─────────────────────────────────────
for category in ["f1", "gt3", "gt4"]:
    results[category] = {}
    tracks = TRACKS[category]
    cars   = CARS[category]

    for track in tracks:
        track_id   = track["id"]
        track_name = track["name"]
        results[category][track_id] = {
            "track_name": track_name,
            "cars": {}
        }

        for car in cars:
            car_id   = car["id"]
            car_name = car["name"]

            prediction = predict_lap_time(category, track_id, car_id)

            if "error" in prediction:
                print(f"[SKIP] {category} / {track_id} / {car_id}: {prediction['error']}")
                continue

            results[category][track_id]["cars"][car_id] = {
                "car_name":           car_name,
                "lap_time":           round(prediction["lap_time"], 3),
                "lap_time_formatted": prediction["lap_time_formatted"],
                "sector_1":           round(prediction["sector_1"], 3),
                "sector_1_formatted": prediction["sector_1_formatted"],
                "sector_2":           round(prediction["sector_2"], 3),
                "sector_2_formatted": prediction["sector_2_formatted"],
                "sector_3":           round(prediction["sector_3"], 3),
                "sector_3_formatted": prediction["sector_3_formatted"],
                "top_speed_kmh":      prediction["top_speed_kmh"],
                "avg_speed_kmh":      prediction["avg_speed_kmh"],
                "confidence":         prediction["confidence"],
            }

            print(f"[OK] {category:4} | {track_id:20} | {car_id:20} | {prediction['lap_time_formatted']}")

# ── Rally ──────────────────────────────────────────────────────────────────
results["rally"] = {}
rally_tracks = TRACKS["rally"]
rally_cars   = CARS["rally"]

for track in rally_tracks:
    track_id   = track["id"]
    track_name = track["name"]
    results["rally"][track_id] = {
        "track_name": track_name,
        "cars": {}
    }

    for car in rally_cars:
        car_id   = car["id"]
        car_name = car["name"]

        prediction = predict_lap_time("rally", track_id, car_id)

        if "error" in prediction:
            print(f"[SKIP] rally / {track_id} / {car_id}: {prediction['error']}")
            continue

        results["rally"][track_id]["cars"][car_id] = {
            "car_name":             car_name,
            "stage_time":           round(prediction["stage_time"], 3),
            "stage_time_formatted": prediction["stage_time_formatted"],
            "ss1_formatted":        prediction["ss1_formatted"],
            "ss2_formatted":        prediction["ss2_formatted"],
            "ss3_formatted":        prediction["ss3_formatted"],
            "top_speed_kmh":        prediction["top_speed_kmh"],
            "avg_speed_kmh":        prediction["avg_speed_kmh"],
            "confidence":           prediction["confidence"],
            "is_rally":             True,
        }

        print(f"[OK] rally | {track_id:20} | {car_id:20} | {prediction['stage_time_formatted']}")

# ── Write output ───────────────────────────────────────────────────────────
out_path = os.path.join(
    os.path.dirname(__file__), "web", "src", "predictions.json"
)
os.makedirs(os.path.dirname(out_path), exist_ok=True)

with open(out_path, "w") as f:
    json.dump(results, f, indent=2)

total = sum(
    len(results[cat][t]["cars"])
    for cat in results
    for t in results[cat]
)
print(f"\n✅ Done — {total} predictions written to {out_path}")
