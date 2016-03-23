"""
Django settings for superlists project.

TO-DO:

"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import json

from django.core.exceptions import ImproperlyConfigured

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

#JSON Based Secret module
with open("secrets.json") as f:
    secrets=json.loads(f.read())

def get_secret(setting,secrets=secrets):
    '''
    This will get the secret variable or return an exception
    '''
    try:
        return secrets[setting]
    except KeyError:
        error_msg="Set {0} environment variable".format(setting)
        raise ImproperlyConfigured(error_msg)

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY=get_secret("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#Once site is moved to production, add the host here.
ALLOWED_HOSTS = ['']

DOMAIN='localhost'
#DOMAIN = 'staging.valueinvestingexchange.com'

ALLOWED_HOSTS=[DOMAIN]


# Application definition

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'djangobower',
    'rest_framework',
    'stockData',
    'accounts',
    'functional_tests',
    'valueFact',
)

AUTH_USER_MODEL = 'auth.User'

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

LOGGING = {
   'version': 1,
   'disable_existing_loggers': False,
   'handlers': {
       'console': {
           'level': 'DEBUG',
           'class': 'logging.StreamHandler',
       },
   },
   'loggers': {
        'django': {
            'handlers': ['console'],
        },
        'accounts': {
            'handlers': ['console'],
        },
        'stockData': {
            'handlers': ['console'],
        },
    },
    'root': {'level': 'INFO'},
}

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'superlists.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
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

WSGI_APPLICATION = 'superlists.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DB_NAME=get_secret("DATABASE_NAME")
DB_USER=get_secret("DATABASE_USERNAME")
DB_PASSWORD=get_secret("DATABASE_PASSWORD")
DB_HOST=get_secret("DATABASE_HOST")
DB_PORT=get_secret("PORT")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_PASSWORD,
        'HOST': DB_HOST,  
        'PORT': DB_PORT,
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
    )
}

#The root directory for all Bower Components

BOWER_COMPONENTS_ROOT = os.path.abspath(os.path.join(BASE_DIR, 'static'))


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT=os.path.abspath(os.path.join(BASE_DIR, '../static'))
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'superlists', 'static'),
    os.path.join(BASE_DIR, 'static'),
)

STATICFILES_FINDERS = (
    'djangobower.finders.BowerFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)


# BOWER Front end applications.  Add as needed

BOWER_INSTALLED_APPS = (
    'underscore',
    "json3#~3.3.1",
    "es5-shim#~3.1.0",
    "font-awesome#4.3.0",

)
