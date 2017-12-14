# Welcome to bookmarks project. It work on django.

You need add file bookmarks/settings_local.py. Example file:
```python
SECRET_KEY = 'TOKEN'
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

# Installing

You must be use Python version 3.6.2. Install Python package with:
```
pip install -r requirements.txt
```
