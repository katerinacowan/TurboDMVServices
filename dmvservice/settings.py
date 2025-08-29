"""
Django settings for dmvservice project.
"""

import os
import sys
from pathlib import Path
from decouple import config, Csv

# Paths
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))

# --- Core security / env ---
SECRET_KEY = config('SECRET_KEY')  # must be set in Heroku config vars
DEBUG = config('DEBUG', default=False, cast=bool)

# Comma-separated in env: "your-app.herokuapp.com,example.com"
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='', cast=Csv()) if not DEBUG else ['*']

# Applications
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',

    # whitenoise support
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',

    'home',
    'django_bootstrap_v5',
    'captcha',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # must be just after SecurityMiddleware
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'dmvservice.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "globalTemplates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'dmvservice.wsgi.application'
ASGI_APPLICATION = 'dmvservice.asgi.application'  # for daphne Procfile

# Database (SQLite, for demo/dev; switch to Postgres in production)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# --- Static files (Heroku-ready) ---
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Only include static dirs that actually exist
candidate_static_dirs = [
    BASE_DIR / "apps/home/static",
    BASE_DIR / "globalStatic",
]
STATICFILES_DIRS = [p for p in candidate_static_dirs if p.exists()]

# Whitenoise storage
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Default PK type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# --- Logging ---
if DEBUG:
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': {'console': {'class': 'logging.StreamHandler'}},
        'root': {'handlers': ['console'], 'level': 'INFO'},
    }
else:
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'verbose': {'format': '{levelname} {asctime} {module} {message}', 'style': '{'},
        },
        'handlers': {
            'console': {'class': 'logging.StreamHandler', 'formatter': 'verbose'},
        },
        'root': {'handlers': ['console'], 'level': 'INFO'},
    }
