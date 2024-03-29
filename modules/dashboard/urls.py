# coding=utf-8

"""
Module Docstring
"""

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from modules.dashboard.views import ChangeLanguageView, DashboardPageView

app_name = 'dashboard'

urlpatterns = [
    path('', DashboardPageView.as_view(), name='dashboard'),
    path('language/', ChangeLanguageView.as_view(), name='change_language'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
