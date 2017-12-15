from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_link, name='index'),
    path('<int:number_links>/', views.get_url),

]
