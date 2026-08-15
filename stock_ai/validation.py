from __future__ import annotations

import pandas as pd

REQUIRED_COLUMNS = {"date", "open", "high", "low", "close", "volume"}


def validate_market_data(df: pd.DataFrame) -> pd.DataFrame:
    missing = REQUIRED_COLUMNS - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    clean = df.copy()
    clean = clean.dropna(subset=["close", "volume"])
    clean = clean.sort_values("date")

    if clean.empty:
        raise ValueError("Dataset is empty after validation")

    return clean
