from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from modules.seller.views import (
	SellerListView,
)
app_name = 'seller'

urlpatterns = [
    path('', SellerListView.as_view(), name='seller_list'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
