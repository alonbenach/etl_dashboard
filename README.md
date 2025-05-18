# 📊 ETL Dashboard with Django, Airflow & Postgres

This project is a self-contained analytics dashboard that demonstrates a working data pipeline built using:

- **Apache Airflow** - for scheduling and running ETL tasks
- **PostgreSQL** - for storing raw event data and aggregated metrics
- **Django** - for building the API and rendering a simple web dashboard
- **Chart.js** - for plotting daily metrics visually

It’s designed as a portfolio-ready ETL project that runs entirely in Docker.

---

## 🚀 Features

- Simulated `Event` data for the last 30 days
- Daily metrics computation using an Airflow DAG
- API access to events and metrics (via Django REST Framework)
- Simple dashboard with tables and interactive charts
- End-to-end orchestration using Docker Compose

---

## 🛠️ Local Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/etl_dashboard.git
cd etl_dashboard
```

### 2. Set Up the Environment
```bash
cp .env.example .env
```

Edit .env to customize the DB name or credentials. These values will be used for both Django and Airflow.

### 3. Build and Run Services
```bash
docker-compose up --build
```
This will:
* build the Django backend
* launch the PostgreSQL DB
* run Airflow webserver and scheduler

Once running:
* Django: http://localhost:8000
* Airflow: http://localhost:8080 (user: admin / pass: admin)

### 4. Initialize Django
```bash
docker-compose exec web bash
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py generate_fake_metrics
```

### 5. Initialize Airflow DB
Open localhost:8080, enable the DAG, and trigger it manually.


### 6. Useful Commands
```bash
# Shell into Django
docker-compose exec web bash

# Run migrations
python manage.py makemigrations
python manage.py migrate
```

### 7. (Optional) Create a Superuser
```bash
docker-compose exec web python manage.py createsuperuser
```

## 📈 Load Demo Data
### Option A: One Command
``` bash
docker-compose exec web python manage.py generate_fake_events
docker-compose exec web python manage.py generate_fake_metrics
```

### Option B: Use Airflow DAG
Visit http://localhost:8080
(default user: airflow, password: airflow)

Enable and trigger daily_metrics_dag to compute metrics from events.

## 🧪 Run Tests
```bash
# Create test data
python manage.py shell
>>> from events.generate_fake_metrics import generate; generate()

# Run tests
docker-compose exec web python manage.py test
```

## 📊 Access the Dashboard
* Django API: http://localhost:8000/api/events/
* Web UI: http://localhost:8000/dashboard/metrics/
* Airflow UI: http://localhost:8080

## 🗂️ Project Structure
```
.
├── backend/
│   ├── config/             # Django settings
│   ├── events/             # Events app
│   │   ├── migrations/
│   │   ├── static/events/js/  # Chart.js scripts
│   │   ├── templates/
│   │   └── management/commands/
│   │       ├── generate_fake_events.py  # Populates the database with fake Event data
│   │       ├── generate_fake_metrics.py    # Populates DailyMetric data for demo/dashboard
│   └── manage.py
├── dags/                   # Airflow DAGs
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env.example
└── README.md
```

## 💬 Notes
* You should not commit your .env file. Rather use the example to create one locally (it will be ignored by .gitignore)
* Static files are collected to staticfiles/ using:
```bash
docker-compose exec web python manage.py collectstatic
```
* If you add new static files or templates, re-run collectstatic.

## 📌 Todo / Future Work
* Add real data ingestion via CSV/API
* Deploy to a cloud platform (Render, Heroku, Railway, EC2)
* Add authentication for dashboard access
* Add CI/CD via GitHub Actions

## 🤝 License
MIT - feel free to use this as a base for your own projects.

