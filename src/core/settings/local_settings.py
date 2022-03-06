"""
Local settings
"""
import os
from pathlib import Path
from core.settings.base_settings import *

print ("Loading *local* settings...")

SECRET_KEY = 'django-insecure-d7f*c#168!-u2zdv%z3+@#q%g9p=@sbfi8-sjgrme2i=olc(vo'
DEBUG = True
ALLOWED_HOSTS = ['*']

INSTALLED_APPS += ['debug_toolbar']

MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']

# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# debug toolbar settings
INTERNAL_IPS = [
    '127.0.0.1',
]

DJANGO_LOG_LEVEL = DEBUG
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "[{levelname} {asctime} Logger: {name}, File: {filename}:{lineno},"
            "\n\t\t\t\t\t\t\t\t\tMessage: {message}",
            "style": "{",
        },
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
    },
    "root": {
        "level": "DEBUG",
        "handlers": ["console"],
    },
    "loggers": {
        # "django.db.backends": {
        #     "handlers": ["console"],
        #     "level": "DEBUG",
        #     "propagate": False,
        # },
        "": {
            "level": "DEBUG",
            "handlers": [
                "console",
            ],
        },
    },
}
