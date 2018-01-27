from django.urls import path
from main.views import *

urlpatterns = [
    path('', index, name='index'),
    path('<int:number_links>/', index),
    path('read/bookmark/<int:bookmark_id>', read_bookmark),
    path('read/bookmark/', read_bookmark),
    path('read/', show_read_bookmarks, name='read'),
    path('search_results/', get_search_results),
]
