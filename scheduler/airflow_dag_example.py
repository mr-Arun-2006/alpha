"""Example Airflow DAG for daily prediction refresh."""

from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="stock_ai_daily_refresh",
    start_date=datetime(2025, 1, 1),
    schedule="0 22 * * 1-5",
    catchup=False,
) as dag:
    run_predict = BashOperator(
        task_id="run_predict",
        bash_command='curl -sS -X POST "http://127.0.0.1:8000/predict?symbol=AAPL"',
    )

    run_predict
