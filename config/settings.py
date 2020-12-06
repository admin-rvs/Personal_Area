import os

from adminlte_base import ThemeLayout, ThemeColor
from django.contrib.messages import constants as message_constants
from django.utils.translation import gettext_lazy as _

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'fl$tv1hsi^#m1p*(mok(sh(4o#q=kkqzi=nbz)06btnr_&u&pv'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
MESSAGE_LEVEL = message_constants.DEBUG

# AdminLTE
ADMINLTE_SITE_TITLE = 'NGS Personal Area'
ADMINLTE_LEGACY_USER_MENU = True
ADMINLTE_MESSAGES_ENABLED = True
ADMINLTE_NOTIFICATIONS_ENABLED = False
ADMINLTE_TASKS_ENABLED = False
ADMINLTE_TERMS_ENDPOINT = 'blank'
ADMINLTE_BRAND_TEXT = 'NGS'
ADMINLTE_LAYOUT = ThemeLayout.DEFAULT | ThemeLayout.FIXED_TOP_NAV | ThemeLayout.FIXED_SIDEBAR
ADMINLTE_BODY_SMALL_TEXT = True
ADMINLTE_SIDEBAR_LIGHT = True
ADMINLTE_LANGUAGE_SWITCHER_ENABLED = False
ADMINLTE_BACK_TO_TOP_ENABLED = True
ADMINLTE_SIDEBAR_CHILD_INDENT = True
ADMINLTE_SIDEBAR_COLOR = ThemeColor.INDIGO
ADMINLTE_FOOTER_SMALL_TEXT = True
# ADMINLTE_USER_MAPPING = AUTH_USER_MODEL
ADMINLTE_BRAND_HTML = '<b>Личный кабинет</b>'

ALLOWED_HOSTS = ['*']

# Application definition
INSTALLED_APPS = [
    'core.apps.CoreConfig',
    # 'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'rest_framework.authtoken',
    'phone_login',
    'django_extensions',
    'crispy_forms',
    'adminlte_full',

]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    )
}

AUTHENTICATION_BACKENDS = [
    'phone_login.backends.phone_backend.PhoneBackend',
    'django.contrib.auth.backends.ModelBackend',
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
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
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'adminlte_full.context_processors.adminlte',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        # 'ENGINE': 'django.db.backends.postgresql_psycopg2',
        # 'NAME': ' ',
        # 'USER': ' ',
        # 'PASSWORD': ' ',
        # 'HOST': '127.0.0.1',
        # 'PORT': '5432',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'Europe/Kiev'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LANGUAGES = [
    ('ru', _('Russian')),
    ('uk', _('Ukrainian')),
    ('en', _('English')),
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(DATA_DIR, 'media')
STATIC_ROOT = os.path.join(DATA_DIR, 'static')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'core', 'static'),
)

# Mail
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

LOGIN_URL = '/login/'
LOGOUT_REDIRECT_URL = '/login/'

# Configure the SENDSMS_BACKEND (for django-sendsms integration)
SENDSMS_BACKEND = 'core.smsbackend.smsclub.SmsBackend'
SENDSMS_FROM_NUMBER = "+XXxxxxxxxxxx"
SENDSMS_ACCOUNT_SID = 'ACXXXXXXXXXXXXXX'
SENDSMS_AUTH_TOKEN = 'xxxxxxxx'

PHONE_LOGIN_ATTEMPTS = 10
PHONE_LOGIN_OTP_LENGTH = 6
PHONE_LOGIN_OTP_HASH_ALGORITHM = 'sha256'
PHONE_LOGIN_DEBUG = True
