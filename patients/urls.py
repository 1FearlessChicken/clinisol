from django.contrib import admin
from django.urls import re_path

#from CBT.students.views import exam_view, login_view, signup_view, disclaimer_view
from patients.views import *

urlpatterns = [
    re_path(r'^$', details_views),
    re_path(r'^details/$', details_views),
    #re_path(r'^disclaimer/(\d+)/$', disclaimer_view),
    #re_path(r'^exam/(\d+)/$', exam_view),
    #re_path(r'^signup/$', signup_view),
]