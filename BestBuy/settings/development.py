"""
Development Settings and Globals
"""


from os import environ
from .base import *
import dj_database_url


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


#     dotenv.load_dotenv(dotenv_file)

########## DEBUG CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = True

ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]


# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
TEMPLATE_DEBUG = DEBUG
########## END DEBUG CONFIGURATION


########## EMAIL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# EMAIL_TIMEOUT = 5
EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST='smtp.gmail.com'
EMAIL_PORT=587
EMAIL_HOST_USER='ceasarkwadwo@gmail.com'
EMAIL_HOST_PASSWORD='Edem12345'
EMAIL_USE_TLS=True
DEFAULT_FROM_EMAIL='ceasarkwadwo@gmail.com'
########## END EMAIL CONFIGURATION

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'CONN_MAX_AGE': 600,
    }
}
# DATABASES = { 'default': dj_database_url.config( default=config('DATABASE_URL') ) }
#DATABASES['default'] = dj_database_url.config(default= 'sqlite:////BASE_DIR/db.sqlite3', conn_max_age=600)


########## CACHE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}
########## END CACHE CONFIGURATION

MEMCACHEIFY_USE_LOCAL=True

# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#internal-ips
INTERNAL_IPS = ["127.0.0.1", "10.0.2.2"]

# Isaiah 30:21