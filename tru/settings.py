"""
Django settings for tru project.

Generated by 'django-admin startproject' using Django 2.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
import django_heroku
from django.contrib.messages import constants as messages

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# PRODUCTION
#SECRET_KEY = os.environ.get('SECRET_KEY')
#DEBUG = (os.environ.get('DEBUG_VALUE') == 'False')

# DEVELOPMENT
SECRET_KEY = 'yr-!bb+ed3*mcx@0@!2+jso61ydy$k8(#xx@4^!0v5^^ky!hd9'
DEBUG = True

#DEBUG_PROPAGATE_EXCEPTIONS = True
TASTYPIE_FULL_DEBUG = True


ALLOWED_HOSTS = ['trututoring.herokuapp.com', 'www.trututoring.live', 'localhost','0.0.0.0']


# Application definition

INSTALLED_APPS = [
    'classroom',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'crispy_forms',
    'widget_tweaks',
    'paypal.standard.ipn',
    #'tempus_dominus',
    #'bootstrap_datepicker_plus',

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

ROOT_URLCONF = 'tru.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
        ],
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

WSGI_APPLICATION = 'tru.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'US/Pacific'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

PAYPAL_RECEIVER_EMAIL = 'trututoring@gmail.com'
PAYPAL_TEST = False

# Sandbox Only
# PAYPAL_RECEIVER_EMAIL = 'sb-w4qen1480916@business.example.com'
# PAYPAL_TEST = True

# Sandbox FYI
# Sandbox personal: sb-dmhln1472476@personal.example.com
# Sandbox password: jNp}"R2%


# Custom Django auth settings

AUTH_USER_MODEL = 'classroom.User'

LOGIN_URL = 'login'

LOGOUT_URL = 'logout'

LOGIN_REDIRECT_URL = 'home'

LOGOUT_REDIRECT_URL = 'home'


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


# Messages built-in framework

MESSAGE_TAGS = {
    messages.DEBUG: 'alert-secondary',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}


# Third party apps configuration

CRISPY_TEMPLATE_PACK = 'bootstrap4'

django_heroku.settings(locals())