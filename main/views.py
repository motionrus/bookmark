from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def list_all_links(request):
    return HttpResponse("it's links")