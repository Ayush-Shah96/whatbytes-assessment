"""
Development Django settings for Healthcare Backend Project.
"""

from .base import *

DEBUG = True
ALLOWED_HOSTS = ['*', 'localhost', '127.0.0.1']

# Development email backend (console)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Development database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'healthcare_db',
        'USER': 'postgres',
        'PASSWORD': 'admin',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Celery in sync mode for development
CELERY_TASK_ALWAYS_EAGER = True

# Logging
LOGGING['root']['level'] = 'DEBUG'
