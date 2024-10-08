import os # noqa
from app.settings.components.base import * # noqa
from app.settings.components.postgres_base import * # noqa


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Для production нужно указать ALLOWED_HOSTS
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '').split(':')

STATIC_ROOT = '/var/www/web_cheatsheets/static'

MEDIA_ROOT = '/var/www/web_cheatsheets/media'
