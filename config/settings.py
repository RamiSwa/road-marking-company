"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 5.0.13.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path

import environ
import os
from storages.backends.s3boto3 import S3Boto3Storage
from distutils.util import strtobool
from django.utils.translation import gettext_lazy as _



# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = os.getenv("SECRET_KEY", "django-insecure-$*-72-ddq(l#ybn*)ll-q51=l_&6y0468w7^9y(x%9ks6iksf^")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(strtobool(os.getenv('DEBUG', 'True')))


ALLOWED_HOSTS = [
    "road-marking-company-production.up.railway.app",
    "localhost",
    "127.0.0.1",
]


CSRF_TRUSTED_ORIGINS = [
    "https://road-marking-company-production.up.railway.app",
    "http://127.0.0.1:8000"
]


# Application definition

INSTALLED_APPS = [
    'modeltranslation',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # ✅ Add missing apps
    'django_celery_results',  # Stores Celery task results in DB
    'django_redis',  # Required for Redis caching
    
    
    # Custom apps
    'core',
    'about',
    'projects',
    'blog',
    'store',
    'contacts',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',  # Enables language switching
    # ✅ Static Files Middleware (for WhiteNoise)
    "whitenoise.middleware.WhiteNoiseMiddleware",

    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases


env = environ.Env()
environ.Env.read_env()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env("POSTGRES_DB", default="railway"),
        'USER': env("POSTGRES_USER", default="postgres"),
        'PASSWORD': env("POSTGRES_PASSWORD"),  # Removed hardcoded password
        'HOST': env("PGHOST", default="shuttle.proxy.rlwy.net"),
        'PORT': env("PGPORT", default="32356"),
    }
}

# Ensure database connection is properly set
if not DATABASES['default']['NAME']:
    raise Exception("PostgreSQL Database not found. Check Railway environment variables.")

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

from django.utils.translation import gettext_lazy as _

# Supported Languages
LANGUAGES = [
    ('en', _('English')),
    ('he', _('Hebrew')),
]

# Default Language
LANGUAGE_CODE = 'en'

# Locale Path (where translations are stored)
# Define where translation files are stored
LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),  # Ensure you have a 'locale' directory
]

# Enable Internationalization & Timezone Settings
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

# Cloudflare R2 Storage Settings

# ✅ Static Files (CSS, JavaScript, Images)
STATIC_URL = '/static/'  # Serve static files locally
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# ✅ WhiteNoise for Optimized Static Files (Keeps Admin Panel Working)
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# ✅ Enable Cloudflare R2 for Media Storage (File Uploads)
USE_CLOUDFLARE_R2 = True  # Ensure R2 is enabled

if USE_CLOUDFLARE_R2:
    DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
    AWS_ACCESS_KEY_ID = os.getenv("R2_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.getenv("R2_SECRET_ACCESS_KEY")
    AWS_STORAGE_BUCKET_NAME = os.getenv("R2_BUCKET_NAME")
    AWS_S3_ENDPOINT_URL = os.getenv("R2_ENDPOINT_URL")

    # ✅ Force Signature Version 4 (to fix unauthorized error)
    AWS_S3_ADDRESSING_STYLE = "virtual"
    AWS_S3_SIGNATURE_VERSION = "s3v4"

    # ✅ Use the custom Cloudflare domain instead of R2.dev
    MEDIA_URL = os.getenv("R2_CUSTOM_DOMAIN", "https://pub-214e66ff75374f66a975fc614da13b39.r2.dev") + "/"
else:
    MEDIA_URL = "/media/"
    MEDIA_ROOT = os.path.join(BASE_DIR, "media")



EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_PORT = os.getenv('EMAIL_PORT')
EMAIL_USE_TLS = bool(strtobool(os.getenv('EMAIL_USE_TLS', 'True')))
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



# Redis for Caching & Celery
# ✅ Redis Cache Configuration
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": os.getenv("REDIS_URL", "redis://default:sygEFwXsJDTUehgOwKEYWQUdPdfffCfO@yamabiko.proxy.rlwy.net:29595"),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}



# ✅ Use Redis as the Celery task broker (message queue)
CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL")
CELERY_RESULT_BACKEND = "django-db"
CELERY_ACCEPT_CONTENT = ["json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_TIMEZONE = "UTC"

