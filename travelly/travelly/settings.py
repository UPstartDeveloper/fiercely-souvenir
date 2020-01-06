"""
Django settings for travelly project.

Generated by 'django-admin startproject' using Django 3.0.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
from dotenv import load_dotenv
import dj_database_url
import django_heroku

load_dotenv()
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

FLIGHT_TITLE_MAX_LENGTH = 600
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = str(os.getenv('SECRET_KEY'))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG', False)

ALLOWED_HOSTS = [
    'localhost',
    'travelly-zr.herokuapp.com',
    '127.0.0.1',
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'trips',
    'airlines',
    'accounts',
    'storages',
    'rest_framework',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'travelly.urls'

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

WSGI_APPLICATION = 'travelly.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'NAME': 'travelly',
        'ENGINE': 'django.db.backends.postgresql',
        'USER': 'postgres',
        'PASSWORD': str(os.getenv('DATABASE_PASSWORD')),
        'HOST': '',
        'PORT': 5432
    }
}


# Login and Logout Redirect Settings
LOGIN_REDIRECT_URL = 'trips:all-trips'
LOGOUT_REDIRECT_URL = 'accounts:login'

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

VALIDATOR_1 = (
    'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'
)
VALIDATOR_2 = (
    'django.contrib.auth.password_validation.MinimumLengthValidator'
)
VALIDATOR_3 = (
    'django.contrib.auth.password_validation.CommonPasswordValidator'
)
VALIDATOR_4 = (
    'django.contrib.auth.password_validation.NumericPasswordValidator'
)
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': VALIDATOR_1},
    {'NAME': VALIDATOR_2},
    {'NAME': VALIDATOR_3},
    {'NAME': VALIDATOR_4},
]

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = [
     os.path.join(BASE_DIR, 'static'),
]

# settings for using AWS S3 file storage
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# Settings for sending email

PASS_1 = os.getenv('EMAIL_PASS_1')
PASS_2 = os.getenv('EMAIL_PASS_2')
PASS_3 = os.getenv('EMAIL_PASS_3')
PASS_4 = os.getenv('EMAIL_PASS_4')

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = str(os.getenv('EMAIL_USERNAME'))
EMAIL_HOST_PASSWORD = f"{PASS_1} {PASS_2} {PASS_3} {PASS_4}"

DEFAULT_FROM_EMAIL = os.getenv('EMAIL_USERNAME')


# provision PostgreSQL for deployment
db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)

# more on deployment
django_heroku.settings(locals())
