from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

from modules.main.views import IndexPageView, ChangeLanguageView
from modules.account.views import LogInView
from modules.dashboard.views import DashboardPageView

urlpatterns = [
    path('', DashboardPageView.as_view(), name='index'),
    path('dashboard/', DashboardPageView.as_view(), name='dashboard'),
    path('backoffice/', admin.site.urls),

    path('language/', ChangeLanguageView.as_view(), name='change_language'),

    path('i18n/', include('django.conf.urls.i18n')),
    path('account/', include('modules.account.urls')),
    path('product/', include('modules.product.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
