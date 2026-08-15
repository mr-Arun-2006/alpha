from __future__ import annotations

from fastapi import FastAPI, HTTPException, Query

from stock_ai.pipeline import run_pipeline
from stock_ai.storage import init_db, latest_predictions

app = FastAPI(title="Stock Market AI Analytics API", version="1.0.0")


@app.on_event("startup")
def startup() -> None:
    init_db()


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.post("/predict")
def predict(symbol: str = Query("AAPL", min_length=1, max_length=10)) -> dict:
    try:
        return run_pipeline(symbol.upper())
    except Exception as exc:  # pragma: no cover
        raise HTTPException(status_code=500, detail=str(exc)) from exc


@app.get("/signals")
def signals(limit: int = Query(20, ge=1, le=200)) -> dict:
    return {"items": latest_predictions(limit)}


@app.get("/metrics")
def metrics(symbol: str = Query("AAPL", min_length=1, max_length=10)) -> dict:
    result = run_pipeline(symbol.upper())
    return {"symbol": symbol.upper(), "metrics": result["metrics"], "mae": result["mae"]}
