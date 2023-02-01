from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls import re_path
from .views import login_view, signup_view, get_name


urlpatterns = [
    re_path(r'^$', login_view),
    re_path(r'^signup/$', signup_view),
    re_path(r'^test/$', get_name),
]
