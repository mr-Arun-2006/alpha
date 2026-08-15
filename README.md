# 🚀 Stock Market AI Analytics System

A ready-to-run starter product for stock analytics with automated ingestion, feature engineering, ML prediction, signal generation, backtesting metrics, and API delivery.

## ✨ What you get
- Automated pipeline (`fetch → validate → features → model → signal → backtest → store`)
- FastAPI backend with prediction + metrics endpoints
- SQLite persistence for generated signals
- Scheduler examples for Cron and Airflow
- Dockerized runtime

## 🧱 Project Structure

```text
.
├── app.py
├── stock_ai/
│   ├── backtest.py
│   ├── data_ingestion.py
│   ├── features.py
│   ├── model.py
│   ├── pipeline.py
│   ├── storage.py
│   ├── strategy.py
│   └── validation.py
├── scheduler/
│   ├── run_pipeline.sh
│   └── airflow_dag_example.py
├── architecture.md
├── codex-usage-plan.md
├── requirements.txt
└── Dockerfile
```

## ⚡ Quick Start (Local)

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app:app --reload
```

API docs: http://127.0.0.1:8000/docs

## 🌐 API Endpoints
- `GET /health` → service status
- `POST /predict?symbol=AAPL` → run full pipeline and store result
- `GET /signals?limit=20` → latest persisted results
- `GET /metrics?symbol=AAPL` → compute fresh model/backtest metrics

## ⏱️ Automation

### Cron
Add a cron entry (example: every weekday 10:00 PM UTC):
```cron
0 22 * * 1-5 /bin/bash /path/to/repo/scheduler/run_pipeline.sh AAPL
```

### Airflow
Use `scheduler/airflow_dag_example.py` as a starting DAG.

## 🐳 Docker

```bash
docker build -t stock-ai .
docker run -p 8000:8000 stock-ai
```

## 🔒 Notes
- This starter uses `yfinance`; production systems should include retry logic, data vendor SLAs, and stronger validation (e.g., Great Expectations).
- Model currently uses RandomForest baseline. XGBoost/LSTM can be plugged into `stock_ai/model.py`.

## 📊 Power BI Integration
- Connect Power BI to API endpoints (`/signals`, `/metrics`) or to an exported table from `data/stock_ai.db`.
- Configure Power BI scheduled refresh after your pipeline schedule.
