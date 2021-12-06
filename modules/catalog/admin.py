from django.contrib import admin
from modules.catalog.product.models import Product, Image, Setting
from modules.catalog.category.models import Category

admin.site.register(Product)
admin.site.register(Image)
admin.site.register(Setting)

admin.site.register(Category)
