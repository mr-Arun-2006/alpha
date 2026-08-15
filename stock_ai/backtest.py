from __future__ import annotations

import numpy as np
import pandas as pd


def calculate_metrics(equity_curve: pd.Series) -> dict[str, float]:
    returns = equity_curve.pct_change().dropna()
    if returns.empty:
        return {"cagr": 0.0, "sharpe": 0.0, "max_drawdown": 0.0}

    periods_per_year = 252
    total_return = equity_curve.iloc[-1] / equity_curve.iloc[0]
    years = len(equity_curve) / periods_per_year
    cagr = (total_return ** (1 / max(years, 1e-9))) - 1

    sharpe = (returns.mean() / returns.std()) * np.sqrt(periods_per_year) if returns.std() else 0.0

    rolling_max = equity_curve.cummax()
    drawdown = (equity_curve - rolling_max) / rolling_max
    max_drawdown = float(drawdown.min())

    return {"cagr": float(cagr), "sharpe": float(sharpe), "max_drawdown": max_drawdown}


def simple_backtest(df: pd.DataFrame) -> dict[str, float]:
    strat_returns = np.where(df["ma10"] > df["ma50"], df["return_1d"], 0.0)
    equity_curve = pd.Series((1 + pd.Series(strat_returns)).cumprod())
    return calculate_metrics(equity_curve)
