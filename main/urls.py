from django.urls import path
from main.views import *

urlpatterns = [
    #path('', index, name='index'),
    path('<int:number_links>/', IndexView.as_view(), name='index'),
    path('search_results/', get_search_results),
    path('generate/', GenerateRandomUserView.as_view(), name='generate'),
    path('', IndexView.as_view(), name='index')
]
