# 🏁 Laptime Predictor

Predict lap times for F1, GT3, GT4, and Rally across real-world circuits.
Runs in your terminal **and** deploys to Vercel as a web app.

---

## Setup

```bash
pip install -r requirements.txt
```

---

## Run — Terminal (CLI)

```bash
python cli/main.py
```

Navigate with number keys. Press `B` to go back at any menu.

---

## Run — Web (local dev)

Open `web/index.html` directly in your browser — it's fully self-contained,
no server needed for the frontend.

To run the API backend locally:

```bash
uvicorn web.api:app --reload --port 8000
```

API docs available at: http://localhost:8000/docs

---

## Deploy to Vercel

1. Push this repo to GitHub
2. Connect to Vercel
3. Set root directory to `/web`
4. Deploy — the `index.html` works as a static site with no backend needed

For the full API deployment on Vercel, add a `vercel.json`:

```json
{
  "builds": [{ "src": "web/api.py", "use": "@vercel/python" }],
  "routes": [{ "src": "/(.*)", "dest": "web/api.py" }]
}
```

---

## Adding ASCII Track Maps

When you have ASCII maps ready:

1. Open `model/data.py`
2. Find the `ASCII_MAPS` dict
3. Add your map using the track `id` as the key

For the web version, open `web/index.html` and find the `ASCII_MAPS` object
in the `<script>` block — add the same maps there.

---

## Project Structure

```
laptime-predictor/
├── cli/
│   └── main.py          ← Terminal app (run this)
├── model/
│   ├── data.py          ← All tracks, cars, ASCII maps
│   └── predictor.py     ← Prediction engine
├── web/
│   ├── index.html       ← Standalone web frontend
│   └── api.py           ← FastAPI backend for Vercel
└── requirements.txt
```

---

## Categories & Tracks

| Category | Tracks | Cars |
|----------|--------|------|
| Formula 1 | 23 | 5 |
| GT3 | 15 | 5 |
| GT4 | 11 | 5 |
| Rally | 10 | 5 |
