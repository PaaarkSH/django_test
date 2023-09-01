#!/bin/bash

python manage.py makemigrations
python manage.py migrate

gunicorn base.wsgi:application --bind 0.0.0.0:8000 --workers 4

