from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import psycopg2
import os

default_args = {
    "owner": "airflow",
    "start_date": datetime(2023, 1, 1),
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}


def compute_metrics():
    print("🚀 START compute_metrics")

    try:
        conn = psycopg2.connect(
            dbname=os.getenv("POSTGRES_DB"),
            user=os.getenv("POSTGRES_USER"),
            password=os.getenv("POSTGRES_PASSWORD"),
            host="db",
            port="5432",
        )
        print("✅ Connected to DB")

        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO events_dailymetric (date, dau, avg_events_per_user)
            SELECT
                DATE(timestamp) AS date,
                COUNT(DISTINCT user_id),
                COUNT(*) * 1.0 / COUNT(DISTINCT user_id)
            FROM events_event
            WHERE DATE(timestamp) = CURRENT_DATE - INTERVAL '1 day'
            GROUP BY DATE(timestamp)
            ON CONFLICT (date) DO NOTHING;
        """
        )
        print("✅ Query executed")

        conn.commit()
        print("✅ Committed")

        cursor.close()
        conn.close()
        print("✅ DB connection closed")

    except Exception as e:
        print(f"❌ ERROR: {e}")


with DAG(
    dag_id="daily_metrics_dag",
    default_args=default_args,
    schedule_interval="@daily",
    catchup=False,
    description="Compute daily user metrics from events",
    tags=["metrics"],
) as dag:
    task = PythonOperator(
        task_id="compute_metrics",
        python_callable=compute_metrics,
    )
