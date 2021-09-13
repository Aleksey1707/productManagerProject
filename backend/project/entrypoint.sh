#!/bin/sh

echo "1) Collect static files"
python manage.py collectstatic --noinput

echo "2) Create cache table"
python manage.py createcachetable

echo "3) Apply migrations"
python manage.py migrate

echo "4) Import test data"
python manage.py import_test_data

echo "5) Run server"
gunicorn project.wsgi:application -b 0.0.0.0:8000
