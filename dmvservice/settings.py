"""
Django settings for dmvservice project (Heroku-ready).
"""

from pathlib import Path
import os
import sys
from decouple import config  # reads env vars (Heroku config vars work with this)

# --------------------------------------------------------------------------------------
# Paths
# --------------------------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, os.path.join(BASE_DIR, "apps"))  # your apps/ directory

# --------------------------------------------------------------------------------------
# Core
# --------------------------------------------------------------------------------------
# Use a real secret in production: heroku config:set SECRET_KEY='...'
SECRET_KEY = config("SECRET_KEY", default="dev-insecure-change-me")  # OK for local dev

DEBUG = config("DEBUG", default=False, cast=bool)

# Accept hosts from env; include Heroku + localhost by default
_default_hosts = "localhost,127.0.0.1,0.0.0.0,*.herokuapp.com"
ALLOWED_HOSTS = [h.strip() for h in config("ALLOWED_HOSTS", default=_default_hosts).split(",") if h.strip()]

# --------------------------------------------------------------------------------------
# Applications
# --------------------------------------------------------------------------------------
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "home",                    # your app
    "django_bootstrap_v5",     # <-- matches the installed package: django-bootstrap-v5
    "captcha",                 # django-simple-captcha
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    # WhiteNoise should be right after SecurityMiddleware
    "whitenoise.middleware.WhiteNoiseMiddleware",

    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "dmvservice.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "globalTemplates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "dmvservice.wsgi.application"
ASGI_APPLICATION = "dmvservice.asgi.application"

# --------------------------------------------------------------------------------------
# Database (SQLite by default; optionally pull DATABASE_URL on Heroku if dj-database-url installed)
# --------------------------------------------------------------------------------------
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Optional Postgres via DATABASE_URL (only if dj-database-url is installed)
if os.environ.get("DATABASE_URL"):
    try:
        import dj_database_url  # not required, only used if present
        DATABASES["default"] = dj_database_url.config(conn_max_age=600, ssl_require=True)
    except Exception:
        # Fall back to SQLite if package not installed
        pass

# --------------------------------------------------------------------------------------
# Password validation
# --------------------------------------------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# --------------------------------------------------------------------------------------
# Internationalization
# --------------------------------------------------------------------------------------
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# --------------------------------------------------------------------------------------
# Static files (WhiteNoise)
# --------------------------------------------------------------------------------------
STATIC_URL = "static/"

# Where collectstatic will put built files on Heroku
STATIC_ROOT = BASE_DIR / "staticfiles"

# Your additional static source dirs (these can exist or not; Django will skip missing)
STATICFILES_DIRS = [
    BASE_DIR / "apps/home/static",
    BASE_DIR / "globalStatic",
]

# WhiteNoise storage: use manifest in production for cache-busting
# If collectstatic ever fails due to missing files, temporarily switch to CompressedStaticFilesStorage
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# --------------------------------------------------------------------------------------
# Default primary key field type
# --------------------------------------------------------------------------------------
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# --------------------------------------------------------------------------------------
# Logging: send to stdout (Heroku logs), not a file
# --------------------------------------------------------------------------------------
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {"format": "%(levelname)s %(name)s: %(message)s"},
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "simple",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "INFO",
    },
}
