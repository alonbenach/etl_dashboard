from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import psycopg2

default_args = {
    "start_date": datetime(2024, 1, 1),
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}


def compute_metrics():
    conn = psycopg2.connect(
        dbname="analytics", user="user", password="pass", host="db", port=5432
    )
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
    conn.commit()
    cursor.close()
    conn.close()


with DAG(
    "daily_metrics",
    default_args=default_args,
    schedule_interval="@daily",
    catchup=False,
) as dag:
    task = PythonOperator(task_id="compute_metrics", python_callable=compute_metrics)
