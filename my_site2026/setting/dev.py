from my_site2026.settings import *
from pathlib import Path




# Development
SECRET_KEY = 'django-insecure-0@od9-$o!e%@2ct&8-@8^)ue_ie91@lue##f!@o8vh1^gtl$%q'

DEBUG = True

ALLOWED_HOSTS = []


# Django Sites
SITE_ID = 2


# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Media
MEDIA_ROOT = BASE_DIR / 'media'


STATICFILES_DIRS = [
    BASE_DIR / "static",
]