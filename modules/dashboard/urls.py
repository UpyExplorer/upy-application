from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import DashboardPageView

app_name = 'dashboard'

urlpatterns = [
    path('', DashboardPageView.as_view(), name='dashboard'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
