from main.models import BookMark
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets


class BookMarkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BookMark
        fields = ('pub_date', 'url', 'site_name', 'title', 'description', 'image', 'user')


class BookMarkViewSet(viewsets.ModelViewSet):
    queryset = BookMark.objects.all()
    serializer_class = BookMarkSerializer


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'bookmark', BookMarkViewSet)
