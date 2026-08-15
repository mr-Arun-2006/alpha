# 🧠 Stock Analytics AI System - Architecture

## 🔷 System Overview
An end-to-end AI-powered stock analytics platform with:
- Automated data pipeline
- ML-based prediction engine
- FastAPI backend
- Dashboard integration path (Power BI/API)

## 🧱 Architecture Layers

### 1. Data Ingestion
- Source: `yfinance` API (extensible to Alpha Vantage)
- Output: Pandas DataFrame → validated dataset

### 2. Data Validation & Preprocessing
- Tools: Pandas (with upgrade path to Great Expectations)
- Tasks: schema checks, null filtering, sort normalization

### 3. Feature Engineering
- Indicators: MA10, MA50, RSI14, volatility20, lag features
- Output: model-ready features and target column

### 4. ML Model Layer
- Baseline included: RandomForestRegressor
- Upgrade path: XGBoost/LightGBM/LSTM
- Output: next-close prediction + MAE

### 5. Strategy Engine
- Decision blend:
  - ML directional prediction
  - MA crossover confirmation
- Output: `BUY` / `SELL` / `HOLD`

### 6. Backtesting Engine
- Included metrics:
  - CAGR
  - Sharpe Ratio
  - Max Drawdown

### 7. Data Storage
- SQLite persistence (`data/stock_ai.db`)
- Stores symbol, date, close, prediction, signal, model error

### 8. API Layer
- Framework: FastAPI
- Endpoints:
  - `POST /predict`
  - `GET /signals`
  - `GET /metrics`
  - `GET /health`

### 9. Automation Layer
- Scheduler options:
  - Cron (sample script included)
  - Airflow (can call pipeline module)

### 10. Visualization Layer
- Power BI can read from API (`/signals`, `/metrics`) or SQLite export jobs

## 🔄 Data Flow
1. Fetch market data
2. Validate/clean records
3. Create features
4. Train model + infer prediction
5. Generate strategy signal
6. Compute backtest metrics
7. Persist result
8. Serve to API consumers/dashboard
