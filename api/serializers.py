from main.models import BookMark
from django.contrib.auth.models import User
from rest_framework import serializers


class BookMarkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BookMark
        fields = ('pk', 'pub_date', 'url', 'site_name', 'title', 'description', 'image', 'user')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')
