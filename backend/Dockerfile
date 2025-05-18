FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y netcat-openbsd

COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

ENV AIRFLOW_VERSION=2.8.1
ENV PYTHON_VERSION=3.10
ENV CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"
RUN pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"

COPY backend/dags /app/dags
COPY . .

ENTRYPOINT ["./entrypoint.sh"]
