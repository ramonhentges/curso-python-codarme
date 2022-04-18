from tamarcado.settings.base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

LOGGING = {
    **LOGGING,
    'loggers': {
        '': {
            'level': 'DEBUG',
            'handlers': ['console']
        }
    }
}
