#!/usr/bin/env sh

python manage.py migrate


gunicorn wsgi:application --bind 0.0.0.0:8000