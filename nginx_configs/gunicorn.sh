#!/bin/bash

# PROJECT_DIR=/app

# cd $PROJECT_DIR
# python manage.py migrate


python manage.py migrate
echo 'Migrations executed'
python manage.py collectstatic --noinput


exec gunicorn memorization_backend.asgi --log-file=- --name=$NAME --log-level=debug --env DJANGO_SETTINGS_MODULE=memorization_backend.settings --bind=:8000 --timeout=500 # -k uvicorn.workers.UvicornWorker
# exec gunicorn memorization_backend.wsgi --bind=:8000