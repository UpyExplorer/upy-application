from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from modules.catalog.product.views import ProductListView, ProductDetailView, ProductUpdateView

app_name = 'catalog'

urlpatterns = [
    path('product/', ProductListView.as_view(), name='product_list'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('product/<int:pk>/edit/', ProductUpdateView.as_view(), name='product_edit'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)