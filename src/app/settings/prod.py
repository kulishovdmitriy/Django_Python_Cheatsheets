import os # noqa
from app.settings.components.base import * # noqa
from app.settings.components.postgres_base import * # noqa
from app.settings.components.email_config import * # noqa
from app.settings.components.celery_broker import * # noqa
from app.settings.components.rest_api import * # noqa
from app.settings.components.all_auth import * # noqa


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Для production нужно указать ALLOWED_HOSTS
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '').split(':')

STATIC_ROOT = '/var/www/web_cheatsheets/static'

MEDIA_ROOT = '/var/www/web_cheatsheets/media'


# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'handlers': {
#         'file': {
#             'level': 'ERROR',
#             'class': 'logging.FileHandler',
#             'filename': '/path/to/your/logs/django-error.log',
#         },
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['file'],
#             'level': 'ERROR',
#             'propagate': True,
#         },
#     },
# }
