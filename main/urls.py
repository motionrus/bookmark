from django.urls import path
from main.views import (
	index,
	get_url,
	)

urlpatterns = [
    path('', index, name='index'),
    path('<int:number_links>/', get_url),
]