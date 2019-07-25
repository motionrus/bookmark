
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('english/', include('book.urls')),
    path('admin/', admin.site.urls),
    path('auth/', include('accounts.urls')),
    path('', include('main.urls')),
    path('api/', include('api.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
