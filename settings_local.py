import os

from settings import *

def env_unset_or_blank(env, value=''):
    e = os.getenv(env, '')
    if e:
        return e
    else:
        return value

DEBUG=False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join('/data','postorius.db')
    }
}

del MAILMAN_USER
del MAILMAN_PASS
del MAILMAN_API_URL

ALLOWED_HOSTS = ['*']

###### POSTORIUS CONFIG
MAILMAN_REST_API_URL = env_unset_or_blank(
            'MAILMAN_REST_API_URL', 'mailman-core:8001')
MAILMAN_REST_API_USER = env_unset_or_blank('MAILMAN_REST_API_USER', 'restadmin')
MAILMAN_REST_API_PASS = env_unset_or_blank('MAILMAN_REST_API_PASS', 'restpass')

EMAIL_HOST = env_unset_or_blank ('POSTORIUS_SMTP_HOST')
EMAIL_PORT = env_unset_or_blank ('POSTORIUS_SMTP_PORT', 25)

EMAIL_HOST_USER =  env_unset_or_blank ('POSTORIUS_SMTP_USER')
EMAIL_HOST_PASSWORD = env_unset_or_blank ('POSTORIUS_SMTP_PASS')
DEFAULT_FROM_EMAIL  = env_unset_or_blank ('POSTORIUS_SMTP_FROM')

EMAIL_USE_TLS = False
use_tls = env_unset_or_blank ('POSTORIUS_SMTP_USE_TLS')
if use_tls == 'TRUE':
    EMAIL_USE_TLS = True

EMAIL_USE_SSL = False
use_ssl = env_unset_or_blank ('POSTORIUS_SMTP_USE_SSL')
if use_ssl == 'TRUE':
    EMAIL_USE_SSL = True

AUTOCREATE_MAILMAN_USER=True

#DEFAULT_FROM_EMAIL = 'postorius@localhost.local'
#SERVER_EMAIL = 'root@localhost.local'
