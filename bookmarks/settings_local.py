import os
from bookmarks.settings import BASE_DIR

SECRET_KEY = 'TOKEN'

# Never deploy a site into production with DEBUG turned on.
# It change to True (strictly for development only).
# Also it settings make your django static files access fail


DEBUG = True
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}