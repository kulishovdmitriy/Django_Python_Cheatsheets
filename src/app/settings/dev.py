from app.settings.components.base import * # noqa
from app.settings.components.dev_tools import * # noqa


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Для production нужно указать ALLOWED_HOSTS
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
