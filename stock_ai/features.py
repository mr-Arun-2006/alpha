from __future__ import annotations

import numpy as np
import pandas as pd


def compute_rsi(series: pd.Series, window: int = 14) -> pd.Series:
    delta = series.diff()
    gain = np.where(delta > 0, delta, 0.0)
    loss = np.where(delta < 0, -delta, 0.0)

    gain_s = pd.Series(gain, index=series.index).rolling(window=window).mean()
    loss_s = pd.Series(loss, index=series.index).rolling(window=window).mean()

    rs = gain_s / loss_s.replace(0, np.nan)
    return 100 - (100 / (1 + rs))


def add_features(df: pd.DataFrame) -> pd.DataFrame:
    feat = df.copy()
    feat["return_1d"] = feat["close"].pct_change()
    feat["ma10"] = feat["close"].rolling(10).mean()
    feat["ma50"] = feat["close"].rolling(50).mean()
    feat["rsi14"] = compute_rsi(feat["close"], 14)
    feat["volatility20"] = feat["return_1d"].rolling(20).std()
    feat["lag1"] = feat["close"].shift(1)
    feat["lag2"] = feat["close"].shift(2)
    feat["target_next_close"] = feat["close"].shift(-1)
    return feat.dropna().reset_index(drop=True)
