from django.urls import path
from main.views import *

urlpatterns = [
    path('', index, name='index'),
    path('<int:number_links>/', index),
    path('search_results/', get_search_results),
]
