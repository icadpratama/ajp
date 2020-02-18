from django.urls import path, re_path
from . import views
from django.urls import include

urlpatterns = [
    re_path('^$', views.list),
    re_path('^detail/$', views.detail),
    path('summernote/', include('django_summernote.urls')),
    path('<str:slug>/', views.detail),
]