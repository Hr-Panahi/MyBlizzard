from blizzard.settings import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-yaricdj-=)f#=7voym3nsnl4knn5)vg6(u&8rcc7(7$cz*+eo@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['blizzard-game-store.ir','www.blizzard-game-store.ir']

#INSTALLED_APPS = []

#sites frameworks
SITE_ID = 3

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blizzard_StoreDB',
        'USER': 'blizzard_StoreUser',
        'PASSWORD': 'H4271024198h',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

STATIC_ROOT = BASE_DIR / '/home/blizzard/public_html/static'
MEDIA_ROOT = BASE_DIR / '/home/blizzard/public_html/media'
STATICFILES_DIRS = [
    BASE_DIR / 'statics'
]

SECURE_BROWSER_XSS_FILTER = True
SECURE_HSTS_SECONDS = 15768000

SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True