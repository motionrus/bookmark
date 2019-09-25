from django.contrib.auth.models import User
from rest_framework import viewsets

from api.serializers import BookMarkSerializer, UserSerializer
from main.models import BookMark


class BookMarkViewSet(viewsets.ModelViewSet):
    queryset = BookMark.objects.all()
    serializer_class = BookMarkSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
