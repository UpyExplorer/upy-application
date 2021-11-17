from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

from modules.main.views import IndexPageView, ChangeLanguageView
from modules.accounts.views import LogInView

urlpatterns = [
    path('backoffice/', admin.site.urls),
    path('', LogInView.as_view(), name='index'),
    path('i18n/', include('django.conf.urls.i18n')),
    path('language/', ChangeLanguageView.as_view(), name='change_language'),
    path('accounts/', include('modules.accounts.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
