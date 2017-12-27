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
        site = BeautifulSoup(r.text, 'html.parser')
        title = site.title.text
        text = site.p.text
        short_text =  site.p.text[:20]
        print('timezone={}, title={}, text={}, short_text={}, '.format(timezone.now(), title, text, short_text))
        BookMark(pub_date=timezone.now(), url=url, title=title, text=text, short_text=short_text).save()


    return form

def save_in_db(request):
    pass


