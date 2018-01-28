
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from accounts import views as accounts_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('accounts.urls')),
    path('links/', include('main.urls')),
    path('', include('main.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

