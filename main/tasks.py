import string

from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from celery import shared_task
from main.html_text_parser import get_url_word_analytics
from main.models import BookMark, Word_Analytics


@shared_task
def save_url_word_analytics(user):
    # Url text analyzer
    current_user = User.objects.get(username=user)
    user_bookmarks = BookMark.objects.filter(user=current_user)
    last_bookmark = user_bookmarks[len(user_bookmarks) - 1]
    url_word_map = get_url_word_analytics(last_bookmark.url)

    for key in url_word_map.keys():
        new_word_analytics = Word_Analytics(
            word=key, frequency=url_word_map.get(key, 0)
        )
        new_word_analytics.bookmark_id = last_bookmark.id
        new_word_analytics.save()


# https://simpleisbetterthancomplex.com/tutorial/2017/08/20/how-to-use-celery-with-django.html
@shared_task
def create_random_user_accounts(total):
    for i in range(total):
        username = 'user_{}'.format(get_random_string(10, string.ascii_letters))
        email = '{}@example.com'.format(username)
        password = get_random_string(50)
        User.objects.create_user(username=username, email=email, password=password)
    return '{} random users created with success!'.format(total)
