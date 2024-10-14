from app.settings.components.base import * # noqa
from app.settings.components.dev_tools import * # noqa
from app.settings.components.celery_broker import * # noqa
from app.settings.components.rest_api import * # noqa


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Для production нужно указать ALLOWED_HOSTS
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
