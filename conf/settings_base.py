from readthedocs.settings.base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'readthedocs',
    }
}

TIME_ZONE = 'Australia/Sydney'
LANGUAGE_CODE = 'en-au'

LANGUAGES = (
    ('en', gettext('English')),
)

SECRET_KEY = 'JFe{4kE9CG0+=-D,dos)_6;[|U5l]B.r<nvZgN#ScOaxh*qzLy'

DEFAULT_FROM_EMAIL = "noreply@3030.com.au"
SESSION_COOKIE_DOMAIN = None

backup_count = 1000
maxBytes = 500 * 100 * 100

ALLOW_PRIVATE_REPOS = True

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTOCOL", "https")

NEWRELIC_ENV = 'development'
