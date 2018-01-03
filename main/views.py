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


def index(request):
    """return last 5 links"""
    form = LinkBookMark()
    if request.method == 'POST':
        add_link(request)
    last_five_links = BookMark.objects.order_by('-pub_date')[:5]
    template = loader.get_template('index.html')
    context = {
        'form': form,
        'response_links': last_five_links,
    }
    return HttpResponse(template.render(context, request))


def get_url(request, number_links):
    link = BookMark.objects.get(pk=number_links)
    format_link = '<h1>{}</h1><p>{}</p>'.format(link.title, link.text)
    return HttpResponse(format_link)


def add_link(request):
    form = LinkBookMark(request.POST)
    if form.is_valid():
        url = (form.cleaned_data['url'])
        r = requests.get(url)
        preview = get_meta_link(url)
        preview['url'] = url
        if not preview['title']:
            site = BeautifulSoup(r.text, 'html.parser')
            preview['title'] = site.title.text
        print('timezone={}, title={title}, image={image}, descr={description}, '.format(timezone.now(), **preview))
        BookMark(pub_date=timezone.now(), **preview).save()
    return form


def get_meta_link(url):
    """return dictionary meta tags"""
    headers = ''
    if 'vk.com' in url:
        # vk.com url is very strange, because without headers is not works
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0'
        }
    dict_meta = {x: '' for x in ['title', 'image', 'description']}
    r = requests.get(url=url, headers=headers)
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, 'html.parser')
        print(soup.find('meta', property='og:'))
        try:
            for key in dict_meta:
                dict_meta[key] = soup.find('meta', property='og:'+key)['content']
        except TypeError:
            pass
    return dict_meta

def save_in_db(request):
    pass


