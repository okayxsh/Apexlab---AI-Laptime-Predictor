"""
Lap Time Predictor - API Backend
FastAPI app deployable on Vercel via serverless functions.
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from model.data import TRACKS, CARS, CATEGORY_LABELS
from model.predictor import predict_lap_time

app = FastAPI(
    title="Lap Time Predictor API",
    description="Predict racing lap times for F1, GT3, GT4, and Rally",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ── Request/Response Models ──────────────────────────────────────────────────

class PredictRequest(BaseModel):
    category: str
    track_id: str
    car_id: str


class PredictResponse(BaseModel):
    success: bool
    category: str
    track_name: str
    car_name: str
    lap_time_formatted: Optional[str] = None
    stage_time_formatted: Optional[str] = None
    sector_1_formatted: Optional[str] = None
    sector_2_formatted: Optional[str] = None
    sector_3_formatted: Optional[str] = None
    ss1_formatted: Optional[str] = None
    ss2_formatted: Optional[str] = None
    ss3_formatted: Optional[str] = None
    top_speed_kmh: int
    avg_speed_kmh: int
    confidence: str
    is_rally: bool = False


# ── Routes ───────────────────────────────────────────────────────────────────

@app.get("/")
def root():
    return {"status": "ok", "message": "Lap Time Predictor API v1.0"}


@app.get("/categories")
def get_categories():
    """Get all available categories"""
    return {
        "categories": [
            {
                "id": cat_id,
                "name": CATEGORY_LABELS[cat_id],
                "track_count": len(TRACKS.get(cat_id, [])),
                "car_count": len(CARS.get(cat_id, [])),
            }
            for cat_id in CATEGORY_LABELS
        ]
    }


@app.get("/tracks/{category}")
def get_tracks(category: str):
    """Get all tracks for a category"""
    if category not in TRACKS:
        raise HTTPException(status_code=404, detail=f"Category '{category}' not found")
    return {"category": category, "tracks": TRACKS[category]}


@app.get("/cars/{category}")
def get_cars(category: str):
    """Get all cars for a category"""
    if category not in CARS:
        raise HTTPException(status_code=404, detail=f"Category '{category}' not found")
    return {"category": category, "cars": CARS[category]}


@app.post("/predict", response_model=PredictResponse)
def predict(req: PredictRequest):
    """Run lap time prediction"""
    # Validate category
    if req.category not in TRACKS:
        raise HTTPException(status_code=400, detail=f"Invalid category: {req.category}")

    # Get track and car names for response
    tracks = TRACKS[req.category]
    cars = CARS[req.category]

    track_obj = next((t for t in tracks if t["id"] == req.track_id), None)
    car_obj = next((c for c in cars if c["id"] == req.car_id), None)

    if not track_obj:
        raise HTTPException(status_code=404, detail=f"Track '{req.track_id}' not found in {req.category}")
    if not car_obj:
        raise HTTPException(status_code=404, detail=f"Car '{req.car_id}' not found in {req.category}")

    result = predict_lap_time(req.category, req.track_id, req.car_id)

    if "error" in result:
        raise HTTPException(status_code=500, detail=result["error"])

    return PredictResponse(
        success=True,
        category=req.category,
        track_name=track_obj["name"],
        car_name=car_obj["name"],
        **{k: v for k, v in result.items() if k not in ("category",)},
    )


@app.get("/predict/{category}/{track_id}/{car_id}")
def predict_get(category: str, track_id: str, car_id: str):
    """GET version of predict for easy testing"""
    return predict(PredictRequest(category=category, track_id=track_id, car_id=car_id))
