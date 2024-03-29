# coding=utf-8

"""
Source App
"""

from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from modules.dashboard.views import DashboardPageView


urlpatterns = [
    path('', DashboardPageView.as_view(), name='dashboard'),
    path('backoffice/', admin.site.urls),

    path('i18n/', include('django.conf.urls.i18n')),
    path('dashboard/', include('modules.dashboard.urls')),
    path('account/', include('modules.account.urls')),
    path('catalog/', include('modules.catalog.urls')),
    path('sale/', include('modules.sale.urls')),
    path('seller/', include('modules.seller.urls')),
    path('customer/', include('modules.customer.urls')),
    path('ads/', include('modules.ads.urls')),
    path('application/', include('modules.application.urls'))
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)
