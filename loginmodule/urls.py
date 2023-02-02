from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls import re_path
#from .views import login_view, signup_view
from .views import d_signup_view #login_view


urlpatterns = [
#    re_path(r'^$', login_view),
 #   re_path(r'^login/$', login_view),
    re_path(r'^signup/$', d_signup_view),
]
