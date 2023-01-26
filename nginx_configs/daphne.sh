#!/bin/bash

python manage.py collectstatic --noinput
python manage.py migrate

# exec daphne memorization_backend.asgi:application -b 0.0.0.0 -p 8000
python manage.py runserver 0.0.0.0:8000