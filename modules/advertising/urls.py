from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from modules.advertising.views import (
	AdvertisingListView,
)
app_name = 'advertising'

urlpatterns = [
    path('', AdvertisingListView.as_view(), name='advertising_list'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)