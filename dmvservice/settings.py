"""
<<<<<<< HEAD
Django settings for dmvservice project.
=======
Django settings for autoDetailProject project.
>>>>>>> 73b0a89400ebc0a3ad2fda240a1674419a4eb18e
"""

import os
import sys
from pathlib import Path
from decouple import config  # .env reader

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))

# -----------------
# SECURITY
# -----------------
SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)
ALLOWED_HOSTS = ['.herokuapp.com', '0.0.0.0', '127.0.0.1', '*']

# -----------------
# APPS
# -----------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # local
    'home',

    # third-party
    'django_bootstrap5',   # ✅ correct app name
    'captcha',
]

# -----------------
# MIDDLEWARE
# -----------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # ✅ must come right after SecurityMiddleware
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

<<<<<<< HEAD
ROOT_URLCONF = 'dmvservice.urls'  # ✅ Fixed from autoDetailProject
=======
ROOT_URLCONF = 'autoDetailProject.urls'
>>>>>>> 73b0a89400ebc0a3ad2fda240a1674419a4eb18e

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

<<<<<<< HEAD
WSGI_APPLICATION = 'dmvservice.wsgi.application'  # ✅ Fixed from TurboDMVServices

# -----------------
# DATABASE (SQLite + Heroku Postgres)
=======
WSGI_APPLICATION = 'TurboDMVServices.wsgi.application'

# -----------------
# DATABASE (SQLite)
>>>>>>> 73b0a89400ebc0a3ad2fda240a1674419a4eb18e
# -----------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

<<<<<<< HEAD
# Override with Heroku database URL if available
import dj_database_url
if 'DATABASE_URL' in os.environ:
    DATABASES['default'] = dj_database_url.parse(os.environ['DATABASE_URL'])

=======
>>>>>>> 73b0a89400ebc0a3ad2fda240a1674419a4eb18e
# -----------------
# PASSWORDS
# -----------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# -----------------
# INTERNATIONALIZATION
# -----------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# -----------------
# STATIC FILES
# -----------------
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / "globalStatic",  # ✅ Cleaned up to avoid duplicates
    # BASE_DIR / "apps/home/static",  # ✅ Commented out to prevent duplicates
]

STATIC_ROOT = BASE_DIR / 'staticfiles'  # ✅ correct target for collectstatic
<<<<<<< HEAD

# ✅ FIXED: Updated to use Django 4.2+ STORAGES setting instead of STATICFILES_STORAGE
STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedStaticFilesStorage",  # ✅ No manifest requirement
    },
}

# -----------------
# MEDIA FILES
# -----------------
MEDIA_URL = '/media/'  # ✅ Added missing MEDIA settings
MEDIA_ROOT = BASE_DIR / 'media'

# -----------------
=======
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# -----------------
>>>>>>> 73b0a89400ebc0a3ad2fda240a1674419a4eb18e
# DEFAULT PK
# -----------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# -----------------
# LOGGING
# -----------------
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/django.log'),
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}
