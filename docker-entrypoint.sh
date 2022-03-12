#!/bin/sh

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate
python manage.py collectstatic --noinput

# Start server
echo "Starting server"
gunicorn core.wsgi:application --log-file -

exec "$@"
