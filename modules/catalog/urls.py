# coding=utf-8

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

from modules.catalog.category.views import (
    CategoryListView
)

app_name = 'catalog'

urlpatterns = [
    path('product/', ProductListView.as_view(), name='product_list'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>', ProductUpdateView.as_view(), name='product_update'),
    path('product/detail/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('product/delete/<int:pk>', ProductDeleteView.as_view(), name='product_delete'),


    path('category/', CategoryListView.as_view(), name='category_list'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
