from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import BookMark
from .forms import LinkBookMark
from django.template import loader

from django.urls import reverse
import requests, re
# Create your views here.


def index(request):
    """return last 5 links"""
    last_five_links = BookMark.objects.order_by('-pub_date')[:5]
    template = loader.get_template('main/index.html')
    context = {
        'response_links': last_five_links,
    }
    return HttpResponse(template.render(context, request))


def get_url(request, number_links):
    link = BookMark.objects.get(pk=number_links)
    format_link = '<h1>{}</h1><p>{}</p>'.format(link.title, link.text)
    return HttpResponse(format_link)

def add_link(request):

    if request.method == 'POST':
        form = LinkBookMark(request.POST)
        
        if form.is_valid():

            return HttpResponseRedirect('/')
    else:
        form = LinkBookMark()

    return render(request, 'main/index.html', {'form': form})

def save_in_db(request):
    pass