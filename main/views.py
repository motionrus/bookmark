from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from main.models import BookMark
from .forms import LinkBookMark
from django.template import loader
from django.utils import timezone
import requests
from bs4 import BeautifulSoup
from django.urls import reverse
from django.views.generic import ListView
# Create your views here.


def last_five_links(index):
    return BookMark.objects.order_by('-pub_date')[index*5:index*5+5]


def index(request, number_links=0):
    """return last 5 links"""
    if request.method == 'POST':
        if 'url' in request.POST:
            parse_link(request)
        if 'delete_pk_id' in request.POST:
            delete_post(request.POST['delete_pk_id'])
    form = LinkBookMark()
    link = last_five_links(number_links)

    number_links_dict = {'prev': number_links - 1, 'current': number_links, 'next': number_links + 1}
    if not last_five_links(number_links + 1):
        number_links_dict.pop('next')

    template = loader.get_template('index.html')
    context = {
        'form': form,
        'response_links': link,
        'number_links': number_links_dict,
    }
    return HttpResponse(template.render(context, request))


def get_url(request, number_links):

    return index(request, number_links)


def parse_link(request):
    form = LinkBookMark(request.POST)
    if form.is_valid():
        url = form.cleaned_data['url']
        html_preview = get_html(url)
        preview = get_meta_tags(html_preview)
        preview['url'] = url
        # logging
        print('\ttimezone={}'.format(timezone.now()))
        for key in preview:
            print('\t{}={}'.format(key, preview[key]))
        BookMark(pub_date=timezone.now(), **preview).save()
    return form


def get_meta_tags(html):
    """return dictionary meta tags"""
    dict_meta = {x: '' for x in ['title', 'image', 'description', 'site_name']}
    soup = BeautifulSoup(html, 'html.parser')
    for key in dict_meta:
        soup_find = soup.find('meta', property='og:'+key)
        if soup_find:
            dict_meta[key] = soup_find['content']
            continue
        soup_find = soup.find('meta', attrs={'name': key})
        if soup_find:
            dict_meta[key] = soup_find['content']
    return dict_meta


def get_html(url):
    headers = ''
    if 'vk.com' in url:
        # vk.com url is very strange, because without headers is not works
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0'
        }
    r = requests.get(url=url, headers=headers)
    if r.status_code == 200:
        return r.text


def save_in_db(request):
    pass


def delete_post(pk_id):
    BookMark.objects.get(pk=pk_id).delete()
    return True
