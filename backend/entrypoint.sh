#!/bin/sh

echo "🕓 Waiting for Postgres..."

while ! nc -z db 5432; do
  sleep 0.1
done

echo "✅ Postgres is up - running migrations"

python manage.py migrate

echo "🚀 Starting Django server"
exec python manage.py runserver 0.0.0.0:8000
