#!/bin/bash

echo "Running Django with ALLOWED_HOSTS: $ALLOWED_HOSTS"

python manage.py runserver 0:"${PORT}" --settings="app.settings.dev"