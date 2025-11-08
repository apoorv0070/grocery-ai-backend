import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SECRET_KEY = 'dev'
DEBUG = True
INSTALLED_APPS = ['django.contrib.admin','django.contrib.auth','django.contrib.contenttypes','django.contrib.sessions','django.contrib.messages','django.contrib.staticfiles','rest_framework','stores','products','ai_engine']
MIDDLEWARE = ['django.middleware.security.SecurityMiddleware','django.contrib.sessions.middleware.SessionMiddleware','django.middleware.common.CommonMiddleware','django.middleware.csrf.CsrfViewMiddleware','django.contrib.auth.middleware.AuthenticationMiddleware','django.contrib.messages.middleware.MessageMiddleware']
ROOT_URLCONF = 'config.urls'
DATABASES = {'default': {'ENGINE': 'django.db.backends.sqlite3','NAME': os.path.join(BASE_DIR, 'db.sqlite3')}}
STATIC_URL = '/static/'
