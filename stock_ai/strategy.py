from __future__ import annotations

import pandas as pd


def generate_signal(latest_row: pd.Series, prediction: float) -> str:
    current_close = float(latest_row["close"])
    ma10 = float(latest_row["ma10"])
    ma50 = float(latest_row["ma50"])

    ml_up = prediction > current_close
    trend_up = ma10 > ma50

    if ml_up and trend_up:
        return "BUY"
    if (not ml_up) and (not trend_up):
        return "SELL"
    return "HOLD"
