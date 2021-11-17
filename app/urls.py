from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

from modules.main.views import IndexPageView, ChangeLanguageView
from modules.accounts.views import LogInView
from modules.dashboard.views import DashboardPageView

urlpatterns = [
    path('backoffice/', admin.site.urls),
    path('', IndexPageView.as_view(), name='index'),
    path('i18n/', include('django.conf.urls.i18n')),
    path('language/', ChangeLanguageView.as_view(), name='change_language'),
    path('accounts/', include('modules.accounts.urls')),
    path('dashboard/', DashboardPageView.as_view(), name='dashboard'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
