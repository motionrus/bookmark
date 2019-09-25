from django.urls import path, include
from rest_framework import routers

from api.views import UserViewSet, BookMarkViewSet
from rest_framework.authtoken import views


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'bookmark', BookMarkViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('token-auth/', views.obtain_auth_token),
]
