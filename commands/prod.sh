#!/bin/bash

echo "Waiting for PostgreSQL to be ready..."

sleep 5

echo "Running Django with ALLOWED_HOSTS: $ALLOWED_HOSTS"
echo "Using Gunicorn with $WORKERS workers on port $PORT"


echo "Applying migrations..."
python manage.py migrate
echo "Migrations applied successfully."


echo "Collecting static files..."
python manage.py collectstatic --noinput
echo "Static files collected successfully."


echo "Starting the application..."
gunicorn -w "${WORKERS}" -b 0.0.0.0:"${PORT}" app.wsgi:application
