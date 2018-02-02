# from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from main.models import BookMark, Word_Analytics
from main.html_text_parser import get_url_word_analytics
from main.forms import LinkBookMark, Search_Form
from django.template import loader
from django.utils import timezone
from bs4 import BeautifulSoup
from django.core.paginator import Paginator
from collections import defaultdict
# from django.urls import reverse
# from django.views.generic import ListView
from django.contrib.auth.models import User
from django.shortcuts import render
import requests
import re
import operator
from urllib.error import URLError
# Create your views here.

DEFAULT_PAGE_SIZE = 6


def index(request, number_links=1, size=DEFAULT_PAGE_SIZE):
    form = LinkBookMark()
    if request.method == 'POST':
        if request.user.is_authenticated is True:
            if 'url' in request.POST:
                form = parse_link(request)
                try:
                    save_url_word_analytics(request)
                except URLError:
                    pass
            elif 'delete_pk_id' in request.POST:
                delete_post(request.POST['delete_pk_id'])
        else:
            print("Non authenticated")
            return HttpResponseRedirect("/login/")
    context = {}
    if request.user.is_authenticated:
        current_user = BookMark.objects.filter(user=request.user)
        page_output = Paginator(
            current_user.order_by('-pub_date'), size).page(number_links)
        context = {
            'form': form,
            'response_links': page_output.object_list,
            'page_output': page_output,
        }
    template = loader.get_template('index.html')

    return HttpResponse(template.render(context, request))


def get_url(request, number_links):
    return index(request, number_links)


def get_search_results(request):
    template = loader.get_template('search_results.html')
    list_results_to_display = []
    search_string = ''

    if request.method == 'POST':
        if request.user.is_authenticated is True:
            _form = Search_Form(request.POST)
            if _form.is_valid():
                form_data = _form.cleaned_data
                search_string = form_data.get("search_parameters")
                if len(search_string) > 0:
                    search_string = clean_search_string(search_string)
                    list_results_to_display = get_searched_bookmarks(
                        search_string, request.user
                    )
            else:
                print("Nothing to search")

    page_output = Paginator(
        list_results_to_display, DEFAULT_PAGE_SIZE
    ).page(1)

    if len(search_string) > 0 and len(list_results_to_display) > 0:
        string_to_display = 'Результаты по вашему запросу: \"' + search_string + '\"'
    elif len(search_string) > 0 and len(list_results_to_display) == 0:
        string_to_display = "Извините, мы ничего не нашли по вашему запросу: \"" + search_string + '\"'
    else:
        string_to_display = "Извините, мы ничего не нашли по вашему запросу"

    context = {
        'search_string': string_to_display,
        'search_results': page_output.object_list,
        'page_output': page_output,
    }
    return HttpResponse(template.render(context, request))


def save_url_word_analytics(request):
    # Url text analyzer
    current_user = User.objects.get(username=request.user.username)
    user_bookmarks = BookMark.objects.filter(user=current_user)
    # last_bookmark_date = user_bookmarks.aggregate(Max('pub_date'))
    # l = BookMark.objects.get(user=request.user, pub_date=last_bookmark_date)
    last_bookmark = user_bookmarks[len(user_bookmarks) - 1]
    url_word_map = get_url_word_analytics(last_bookmark.url)

    for key in url_word_map.keys():
        new_word_analytics = Word_Analytics(
            word=key, frequency=url_word_map.get(key, 0)
        )
        new_word_analytics.bookmark_id = last_bookmark.id
        new_word_analytics.save()


def get_searched_bookmarks(_search_string, _user):

    user_bookmarks = BookMark.objects.filter(user=_user)
    bookmark_search_results = defaultdict(lambda: 0)

    for bookmark in user_bookmarks:
        results = Word_Analytics.objects.filter(
            bookmark=bookmark
        ).filter(
            word__in=(_search_string.split())
        )

        if len(results) > 0:
            for res in results:
                print(res)
                if bookmark.id in bookmark_search_results.keys():
                    bookmark_search_results[bookmark.id] += res.frequency
                else:
                    bookmark_search_results[bookmark.id]

    results_to_display = []
    if len(bookmark_search_results) > 0:
        # sort the results of search
        bookmark_search_results_sorted = sorted(
            bookmark_search_results.items(), key=operator.itemgetter(1),
            reverse=True
        )
        # add sorted results to a list to display
        for result in bookmark_search_results_sorted:
            results_to_display.append(BookMark.objects.get(id=result[0]))

    return results_to_display


def clean_search_string(search_string):
    search_string_cleaned = re.sub(
        '[^A-Za-zа-яА-Я0-9 ]', '', search_string.lower()
    )
    print(search_string_cleaned)
    return search_string_cleaned


def parse_link(request):
    form = LinkBookMark(request.POST)
    if form.is_valid():
        url = form.cleaned_data['url']
        html_preview = get_html(url)
        preview = get_meta_tags(html_preview)
        preview['url'] = url
        current_user = User.objects.get(username=request.user.username)
        preview['user'] = current_user
        # for key in preview:
        #     print('\t{}={}'.format(key, preview[key]))
        BookMark(pub_date=timezone.now(), **preview).save()

    return form


def get_meta_tags(html):
    """return dictionary meta tags"""
    dict_meta = {x: '' for x in ['title', 'image', 'description', 'site_name']}
    soup = BeautifulSoup(html, 'html.parser')
    for key in dict_meta:
        soup_find = soup.find('meta', property='og:' + key)
        if soup_find:
            dict_meta[key] = soup_find['content']
            continue
        soup_find = soup.find('meta', attrs={'name': key})
        if soup_find:
            dict_meta[key] = soup_find['content']
    return dict_meta


def get_html(url):
    from requests.exceptions import ConnectionError, ConnectTimeout
    headers = ''
    if 'vk.com' in url:
        # vk.com url is very strange, because without headers is not works
        headers = {
            'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0'
        }
    try:
        r = requests.get(url=url, headers=headers, timeout=10)
    except (ConnectTimeout, ConnectionError):
        return ''
    if r.status_code == 200:
        return r.text


def delete_post(pk_id):
    BookMark.objects.get(pk=pk_id).delete()
    return True
