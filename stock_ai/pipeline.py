from __future__ import annotations

from stock_ai.backtest import simple_backtest
from stock_ai.data_ingestion import fetch_history
from stock_ai.features import add_features
from stock_ai.model import PredictionModel
from stock_ai.storage import init_db, save_prediction
from stock_ai.strategy import generate_signal
from stock_ai.validation import validate_market_data


def run_pipeline(symbol: str = "AAPL") -> dict:
    raw = fetch_history(symbol)
    clean = validate_market_data(raw)
    feat = add_features(clean)

    model = PredictionModel()
    model_out = model.train_and_predict(feat)

    latest = feat.iloc[-1]
    signal = generate_signal(latest, model_out.prediction)
    metrics = simple_backtest(feat)

    init_db()
    save_prediction(
        symbol=symbol,
        as_of_date=str(latest["date"]),
        close_price=float(latest["close"]),
        predicted_next_close=model_out.prediction,
        signal=signal,
        mae=model_out.mae,
    )

    return {
        "symbol": symbol,
        "as_of_date": str(latest["date"]),
        "close": float(latest["close"]),
        "predicted_next_close": model_out.prediction,
        "signal": signal,
        "mae": model_out.mae,
        "metrics": metrics,
    }
