from app.settings.components.base import INSTALLED_APPS, MIDDLEWARE


INSTALLED_APPS += [
    'debug_toolbar',
    'django_extensions',  # Позволяет выполнять SQL запросы к нашей базе с терминала(создавать объекты, редактировать, удалять)
]

# Добавление промежуточного слоя (middleware)
MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

# Для корректной работы панели отладки, нужно указать список допустимых IP-адресов. В dev-среде можно просто добавить локальный IP:
INTERNAL_IPS = [
    '127.0.0.1',
]
