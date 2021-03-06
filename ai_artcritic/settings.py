"""
Django settings for ai_artcritic project.

Generated by 'django-admin startproject' using Django 2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^^lbm7ho-s#=%^=-3z@4#4d30@1gfrf=w12o8e1g_%rm!!0!hl'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'critic',
    'storages', 
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

ROOT_URLCONF = 'ai_artcritic.urls'

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

WSGI_APPLICATION = 'ai_artcritic.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/


STATIC_URL = '/static/'
STATIC_ROOT = 'static/'

#MEDIA_ROOT = STATIC_ROOT + 'media'
#MEDIA_URL =  '/media/'

PROJECT_ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir)

environment = 'prod'
if environment == 'local':
    DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
    
    #STATIC_ROOT = 'static/'
    #STATIC_URL = '/static/'
    
    MEDIA_ROOT = STATIC_ROOT + 'media'
    MEDIA_URL = '/media/'
    
    UPLOAD_ROOT = 'uploads/'
    
    #DOWNLOAD_URL = STATIC_URL + "media/downloads"
    #DOWNLOAD_ROOT = os.path.join(PROJECT_ROOT, "static/media/downloads")
# for prod environment
else: 
    DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
    STATICFILES_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
    
    GS_PROJECT_ID = 'ai-art-critic'
    GS_STATIC_BUCKET_NAME = 'critic_media'
    GS_MEDIA_BUCKET_NAME = 'critic_media'  # same as STATIC BUCKET if using single bucket both for static and media
    GS_BUCKET_NAME = 'critic_media'
    GS_DEFAULT_ACL = 'publicRead'
    GS_FILE_OVERWRITE = False
    
    # STATIC_URL = 'https://storage.googleapis.com/{}/'.format(GS_STATIC_BUCKET_NAME)
    # STATIC_ROOT = "static/"

    MEDIA_URL = 'https://storage.googleapis.com/{}/'.format(GS_MEDIA_BUCKET_NAME)
    MEDIA_ROOT = "media/"
    
    UPLOAD_ROOT = 'media/uploads/'
    
    #DOWNLOAD_ROOT = os.path.join(PROJECT_ROOT, "static/media/downloads")
    #DOWNLOAD_URL = STATIC_URL + "media/downloads"