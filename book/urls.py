from django.urls import *
from book.views import *
from django.conf.urls import url

urlpatterns = [
    url('^imlegend/(?P<page>[0-9]{1,3})/$', imlegend, name='imlegend'),
    url('^imlegend/$', imlegend, name='imlegend'),
    url('^$', index, name='index')
]

