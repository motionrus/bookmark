from django.urls import path, include
from main.views import *
from .serializers import router


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]