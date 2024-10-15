from datetime import timedelta

from app.settings.components.base import INSTALLED_APPS


INSTALLED_APPS += [

    'rest_framework',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),

    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],

    'DEFAULT_THROTTLE_RATES': {
        'user': '5/min',
        'anon': '5/min',
    },

    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.UserRateThrottle',
        'rest_framework.throttling.AnonRateThrottle',
    ],
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=15),  # Время жизни access-токена
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),     # Время жизни refresh-токена
    'BLACKLIST_AFTER_ROTATION': True,                 # Использовать черный список после обновления
    'UPDATE_LAST_LOGIN': True,                        # Обновить время последнего входа
}
