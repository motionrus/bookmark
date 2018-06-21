from django.urls import path, include, re_path
from accounts import views as accounts_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', accounts_views.signup, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('password_reset/', auth_views.password_reset, name='password_reset'),
    path('password_reset/done', auth_views.password_reset_done, name='password_reset_done'),
    re_path(r'reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',
            auth_views.password_reset_confirm, name='password_reset_confirm'),
    path('reset/done/', auth_views.password_reset_complete, name='password_reset_complete'),
]
