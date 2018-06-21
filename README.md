# Welcome to bookmarks project.

 - The goal of the project is to allow users to store all the links in one place.

## New Features
Currently, previews and smart searches are supported. This project uses Django 2.0 and Python version 3.6.2. Requests are written to the database and processed by the library in parallel. NTLK allows you to highlight keywords and implement smart search


### Installation

Create a new environment and install requirements

```sh
$ mkdir bookmark
$ cd bookmark/
$ python3 -m venv venv
$ git clone https://github.com/rus-vista/bookmark.git
$ source venv/bin/activate
$ pip install -r bookmark/requirements.txt
```

### Run

Create new DB(SQLite) and start project

```sh
$ cd bookmark
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
...
Django version 2.0, using settings 'bookmarks.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

### Production

You need to add a file bookmarks/settings_local.py.
Example of a production file with a postgres:

```python
SECRET_KEY = 'TOKEN'
DEBUG = False
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

### About me

If you have any suggestions or wishes, you can send me a message in the telegram [@motionrus](https://t.me/motionrus)