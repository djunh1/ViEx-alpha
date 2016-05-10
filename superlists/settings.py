"""
Django settings for superlists project.

TO-DO:

"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import json

from django.core.exceptions import ImproperlyConfigured
from django.core.urlresolvers import reverse_lazy

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
    'accounts',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'social.apps.django_app.default',
    'djangobower',
    'rest_framework',
    'functional_tests',
    'valueFact',
)

#Find out about social app auth module, this one doesnt work.

AUTHENTICATION_BACKENDS = (
    'social.backends.facebook.Facebook2OAuth2',
    'social.backends.google.GoogleOAuth2',
    'social.backends.twitter.TwitterOAuth',
    'django.contrib.auth.backends.ModelBackend',
    'accounts.authentication.EmailAuthBackend'
)

SOCIAL_AUTH_FACEBOOK_KEY = '502940859892957'
SOCIAL_AUTH_FACEBOOK_SECRET = 'fd2135cdd771a1ea4f8aa852d432adac'
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']

SOCIAL_AUTH_TWITTER_KEY = 'nJOw11Pppi2x6Jr8U8SxnDtGl'
SOCIAL_AUTH_TWITTER_SECRET = 'NTa0K0iURh5GEX2X9Ofy7OtJN1hYEgAmYPMhjxE0vQ0BwH9XCo'

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '670034875011-ndl8i38o956jf1a1muqb456b93bb45a5.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'js0AOlAwrvO15T6ZEGWiwWPl'


LOGIN_REDIRECT_URL = reverse_lazy('dashboard')
LOGIN_URL = reverse_lazy('login')
LOGOUT_URL = reverse_lazy('logout')

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


WSGI_APPLICATION = 'superlists.wsgi.application'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DB_NAME = get_secret("DATABASE_NAME")
DB_USER = get_secret("DATABASE_USERNAME")
DB_PASSWORD = get_secret("DATABASE_PASSWORD")
DB_HOST = get_secret("DATABASE_HOST")
DB_PORT = get_secret("PORT")

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


# Email settings

email_host = get_secret("EMAIL_HOST")
email_host_user = get_secret("EMAIL_HOST_USER")
email_to_user = get_secret("EMAIL_TO_USER")
email_host_password = get_secret("EMAIL_HOST_PASSWORD")

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = email_host
EMAIL_HOST_USER = email_host_user
EMAIL_HOST_PASSWORD = email_host_password
DEFAULT_FROM_EMAIL = email_host_user
DEFAULT_TO_EMAIL = email_to_user
SERVER_EMAIL = email_host_user
EMAIL_PORT = 587
EMAIL_USE_TLS = True


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

#Site map
SITE_ID = 1

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

