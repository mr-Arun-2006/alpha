from __future__ import annotations

import pandas as pd
import yfinance as yf


def fetch_history(symbol: str, period: str = "2y", interval: str = "1d") -> pd.DataFrame:
    """Fetch OHLCV history for a ticker via yfinance."""
    ticker = yf.Ticker(symbol)
    df = ticker.history(period=period, interval=interval, auto_adjust=True)
    if df.empty:
        raise ValueError(f"No data returned for symbol={symbol}")

    df = df.rename(columns=str.lower)
    df.index.name = "date"
    return df.reset_index()
