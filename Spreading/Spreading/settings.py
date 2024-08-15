"""
Django settings for Spreading project.

Generated by 'django-admin startproject' using Django 5.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

import os
from pathlib import Path

# import pymongo
from django.contrib import messages
from dotenv import load_dotenv
from django.conf import settings
import logging

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv()
logger = logging.getLogger(__name__)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY", "default-secret-key")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False


# ENVIRONMENT = os.getenv('DJANGO_ENVIRONMENT', 'local')  # Default to 'local' if not set

# if ENVIRONMENT == 'production':
#     from .production import *
# elif ENVIRONMENT == 'local':
#     from .local import *
# else:
#     from .base import *

ALLOWED_HOSTS = ["charity-production-8168.up.railway.app","charity-production-8168.up.railway.app", "127.0.0.1", "8000"]
logger.debug(ALLOWED_HOSTS)
CSRF_TRUSTED_ORIGINS = ["https://charity-production-8168.up.railway.app",]






# Loggings

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {process:d} {message}',
            'style': '{',
        },
    },

    'handlers': {
        'newfile': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': './debug.log',
            'formatter': 'verbose'
        },
    },

    'loggers': {
        '': {
            'level': 'DEBUG',
            'handlers': ['newfile'],
            'propagate': True,
        },
    },

}






# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main_app',

    # other apps
    "Payment",
    "whitenoise.runserver_nostatic",
    

    # extensions
    "crispy_forms",
    "crispy_bootstrap5",
    "django.contrib.humanize",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'Spreading.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'Spreading.wsgi.application'



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'defaultdb',
        'USER': 'avnadmin',
        'PASSWORD': os.environ['DB_PASSWORD'],
        'HOST': 'smilesdb-wangaraali56-4122.l.aivencloud.com',
        'PORT': '11603',
        'OPTIONS': {
            'sslmode': 'require',
        },
    }
}







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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATIC_ROOT = BASE_DIR / 'static'

# white noise static stuffs
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'


STATIC_ROOT = BASE_DIR/ 'staticfiles'

STATICFILES_DIRS = [
    BASE_DIR/ 'main_app'/'assets',
]

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

CRISPY_TEMPLATE_PACK = "bootstrap5"

MESSAGE_TAGS = {
    messages.SUCCESS: "alert-success",
    messages.INFO: "alert-info",
    messages.ERROR: "alert-danger",
    messages.DEBUG: "alert-dark",
    messages.WARNING: "alert-warning",
}


MPESA_API = {
    "BIZ_SHORT_CODE" : os.environ.get("BIZ_SHORT_CODE"),
    "CALLBACK_URL":os.environ.get("CALLBACK_URL"),
    "CONSUMER_KEY": os.environ.get("CONSUMER_KEY"),
    "CONSUMER_SECRET": os.environ.get("CONSUMER_SECRET"),
    "CREDENTIALS_URL": os.environ.get("CREDENTIALS_URL"),
    "PAYMENT_URL": os.environ.get("PAYMENT_URL"),
    "PASS_KEY":os.environ.get("PASS_KEY")
}


EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
EMAIL_HOST_USER =os.environ.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD =os.environ.get("EMAIL_HOST_PASSWORD")
