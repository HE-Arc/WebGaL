import os
import sys

# Auth vars
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

#  registration hmac workflow settings
ACCOUNT_ACTIVATION_DAYS = 7
# next two stteings already have those values by default
# REGISTRATION_OPEN = True
# REGISTRATION_SALT = "registration"

# PATH vars

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
root = lambda *x: os.path.join(BASE_DIR, *x)
PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))
TEMPLATE_PATH = PROJECT_PATH + '/main/templates/'

sys.path.insert(0, root('apps'))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'CHANGE THIS!!!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
IN_TESTING = sys.argv[1:2] == ['test']

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main',
    'materialize',
    'django.contrib.sites',
    'django_comments'
]

SITE_ID = 1

PROJECT_APPS = []

INSTALLED_APPS += PROJECT_APPS

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'WebGal.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'WebGal.wsgi.application'

# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'WebGal',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': '',  # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',  # Set to empty string for default.
    }
}

FIXTURES_DIRS = (
    PROJECT_PATH + 'fixtures/',
)

# Internationalization

LANGUAGE_CODE = 'en-gb'

TIME_ZONE = 'UTC'

USE_I18N = False

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_ROOT = os.path.join(PROJECT_PATH, '../main/static')

STATIC_URL = '/static/'

# Additional locations of static files

STATICFILES_DIRS = (
    root('assets'), os.path.join(BASE_DIR, "../main/static"),

)
MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'DIRS': [
            root('templates'), TEMPLATE_PATH,
            os.path.join(os.path.dirname(os.path.dirname(PROJECT_PATH)), MEDIA_ROOT + '/media/')
        ],
        'OPTIONS': {
            'debug': DEBUG,
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    }
]

FILE_UPLOAD_HANDLERS = [
    "django.core.files.uploadhandler.MemoryFileUploadHandler",
    "django.core.files.uploadhandler.TemporaryFileUploadHandler"
]

# Password validation

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

# .local.py overrides all the common settings.
try:
    from .local import *  # noqa


    INSTALLED_APPS.append('debug_toolbar')
    MIDDLEWARE_CLASSES.insert(
        0, 'debug_toolbar.middleware.DebugToolbarMiddleware')
except ImportError:
    pass

# importing test settings file if necessary
if IN_TESTING:
    from .testing import *  # noqa

# overide with production.py if not in DEBUG mode
if not DEBUG:
    from .production import *
