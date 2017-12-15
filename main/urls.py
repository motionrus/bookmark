from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:number_links>/', views.get_url),
]
