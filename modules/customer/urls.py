# coding=utf-8

"""
Module Docstring
"""

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from modules.customer.views import CustomerListView


app_name = 'customer'

urlpatterns = [
    path('', CustomerListView.as_view(), name='customer_list'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
