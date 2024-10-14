#!/bin/bash

echo "Awaiting RabbitMQ ..."

sleep 20

echo "Launch Celery ..."

celery -A app worker -l info -c "$CELERY_NUM_WORKERS"