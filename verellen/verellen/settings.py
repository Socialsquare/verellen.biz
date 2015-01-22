"""
Django settings for verellen project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

import logging
import os
from django.contrib import messages

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SITE_ID = 1

SECRET_KEY = '&pb13g0lcs(i$=&6928+ey_z#v4#@dz@4i8l2#5kx%gf@dt*#u'

ALLOWED_HOSTS = []

# Application definition

TEMPLATE_DIRS = (
     os.path.join(os.path.dirname(__file__), 'templates'),
)

INSTALLED_APPS = (
    'grappelli.dashboard',
    'grappelli',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'south',
    'tinymce',
    'storages',
    'sorl.thumbnail',

    'verellen',
    'products',
    'retailers',
    'partner',
    'content',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'verellen.urls'

WSGI_APPLICATION = 'verellen.wsgi.application'


# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',

    'content.context_preprocessor.content'
)

# Internationalization

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Grappelli
ADMIN_MEDIA_PREFIX = "admin/"
GRAPPELLI_ADMIN_TITLE = "Verellen administration"
GRAPPELLI_SWITCH_USER = True
GRAPPELLI_INDEX_DASHBOARD = 'dashboard.CustomIndexDashboard'

# Static/media

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

# TinyMCE config
TINYMCE_DEFAULT_CONFIG = {
    'theme_advanced_buttons1' : 'bold, italic, underline, fontsizeselect, justifyleft, justifycenter, justifyright, bullist, link, unlink, undo, redo, code',
    'theme_advanced_buttons2' : '',
    'theme_advanced_buttons3' : '',

    'theme': 'advanced',
    'width': 700
}

# sorl thumnail config
THUMBNAIL_PREFIX = 'thumbnail_cache/'

# make message tag play along with bootstrap
MESSAGE_TAGS = {
    messages.ERROR: 'danger',
}

try:
    from local_settings import *
except ImportError:
    pass
