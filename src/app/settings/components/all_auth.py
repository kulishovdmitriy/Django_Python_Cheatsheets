from app.settings.components.base import INSTALLED_APPS, MIDDLEWARE


INSTALLED_APPS += [
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    'allauth.socialaccount.providers.github',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.facebook',
]

MIDDLEWARE += [
    "allauth.account.middleware.AccountMiddleware",
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',  # Для входа через имя пользователя
    'allauth.account.auth_backends.AuthenticationBackend',  # Для входа через email
]

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        # For each OAuth based provider, either add a ``SocialApp``
        # (``socialaccount`` app) containing the required client
        # credentials, or list them here:
        'APP': {
            'client_id': '123',
            'secret': '456',
            'key': ''
        }
    },

    'github': {
        'APP': {
            'client_id': 'your_github_client_id',
            'secret': 'your_github_client_secret',
            'key': ''
        }
    },

    'facebook': {
        'APP': {
            'client_id': 'your_facebook_client_id',
            'secret': 'your_facebook_client_secret',
            'key': ''
        }
    }
}

SITE_ID = 1

ACCOUNT_EMAIL_REQUIRED = True  # Требовать email
# ACCOUNT_EMAIL_VERIFICATION = 'mandatory'  # Обязательная верификация email
ACCOUNT_USERNAME_REQUIRED = False  # Отключить требование имени пользователя
ACCOUNT_AUTHENTICATED_LOGIN_REDIRECTS = True  # Перенаправление после входа
ACCOUNT_AUTHENTICATION_METHOD = 'email'  # Вход только по email
