#!/bin/bash

# Apply database migrations
echo "Apply database migrations"
poetry run python manage.py migrate
poetry run python manage.py collectstatic --noinput

# Start server
echo "Starting server"
poetry run gunicorn core.wsgi:application --bind 0.0.0.0:8000

exec "$@"
