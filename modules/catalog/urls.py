from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from modules.catalog.product.views import (
	ProductListView,
	ProductDetailView,
	ProductUpdateView,
	ProductCreateView,
	ProductDeleteView
)

app_name = 'catalog'

urlpatterns = [
    path('product/', ProductListView.as_view(), name='product_list'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>', ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/detail/', ProductDetailView.as_view(), name='product_detail'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)