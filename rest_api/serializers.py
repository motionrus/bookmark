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


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'bookmark', BookMarkViewSet)