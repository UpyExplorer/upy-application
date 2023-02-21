# coding=utf-8

"""
Url Application
"""

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from modules.application.views import ApplicationListView


app_name = 'application'

urlpatterns = [
    path('', ApplicationListView.as_view(), name='application_list')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
