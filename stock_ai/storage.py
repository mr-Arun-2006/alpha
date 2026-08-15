from __future__ import annotations

import sqlite3
from pathlib import Path

DB_PATH = Path("data/stock_ai.db")


def init_db() -> None:
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS predictions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                symbol TEXT NOT NULL,
                as_of_date TEXT NOT NULL,
                close_price REAL NOT NULL,
                predicted_next_close REAL NOT NULL,
                signal TEXT NOT NULL,
                mae REAL NOT NULL,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            )
            """
        )


def save_prediction(symbol: str, as_of_date: str, close_price: float, predicted_next_close: float, signal: str, mae: float) -> None:
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            """
            INSERT INTO predictions(symbol, as_of_date, close_price, predicted_next_close, signal, mae)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (symbol, as_of_date, close_price, predicted_next_close, signal, mae),
        )


def latest_predictions(limit: int = 50) -> list[dict]:
    with sqlite3.connect(DB_PATH) as conn:
        conn.row_factory = sqlite3.Row
        rows = conn.execute(
            "SELECT * FROM predictions ORDER BY id DESC LIMIT ?",
            (limit,),
        ).fetchall()
    return [dict(r) for r in rows]
