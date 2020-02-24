from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from news import views as news_view
from event import views as event_view

from . import views

urlpatterns = [
    path('', views.home_page),
    path('contact/', views.contact_page),
    path('party/', views.party_page),
    path('maso/', admin.site.urls),
    path('news/', include('news.urls')),
    path('event/', include('event.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "AJP Admin"
admin.site.site_title = "AJP Admin Portal"
admin.site.index_title = "Welcome to AJP Website Portal"