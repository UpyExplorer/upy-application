# coding=utf-8

"""
Module Docstring
"""

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from modules.sale.order.views import OrderListView


app_name = 'sale'

urlpatterns = [
    path('order/', OrderListView.as_view(), name='order_list'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
