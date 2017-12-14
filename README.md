# Welcome to bookmarks project. It work on django.

You need add file bookmarks/settings_local.py. Example file:
```
# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = '%#$!s*#*fpn@oprip9hixna0v_osjvgk4ahc-%fvb7mti*t1x&'


# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = True


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'name_db',
        'USER': 'name_user',
        'PASSWORD': 'password',
        'HOST': 'ip-address or host',
        'PORT': '5432',
    }
}

```