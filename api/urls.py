from django.urls import path, include
from .serializers import router
from rest_framework.authtoken import views

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('token-auth/', views.obtain_auth_token),
]
