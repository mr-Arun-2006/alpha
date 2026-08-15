from __future__ import annotations

from dataclasses import dataclass

import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

FEATURE_COLUMNS = ["ma10", "ma50", "rsi14", "volatility20", "lag1", "lag2"]


@dataclass
class ModelOutput:
    prediction: float
    mae: float


class PredictionModel:
    def __init__(self) -> None:
        self.model = RandomForestRegressor(
            n_estimators=300,
            random_state=42,
            min_samples_leaf=2,
        )

    def train_and_predict(self, data: pd.DataFrame) -> ModelOutput:
        x = data[FEATURE_COLUMNS]
        y = data["target_next_close"]

        split_idx = int(len(data) * 0.8)
        x_train, x_test = x.iloc[:split_idx], x.iloc[split_idx:]
        y_train, y_test = y.iloc[:split_idx], y.iloc[split_idx:]

        self.model.fit(x_train, y_train)

        test_preds = self.model.predict(x_test)
        mae = mean_absolute_error(y_test, test_preds)

        latest_features = x.iloc[[-1]]
        next_close = float(self.model.predict(latest_features)[0])
        return ModelOutput(prediction=next_close, mae=float(mae))
