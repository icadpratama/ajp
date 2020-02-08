from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path('^$', views.list),
    re_path('^detail/$', views.detail),
]