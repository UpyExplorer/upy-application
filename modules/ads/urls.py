from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from modules.ads.views import (
	AdsListView,
)
app_name = 'ads'

urlpatterns = [
    path('', AdsListView.as_view(), name='ads_list'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)