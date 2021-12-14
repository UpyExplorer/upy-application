from django.contrib import admin
from app.base import get_field_list
from modules.catalog.product.models import (
    Product,
    Image,
    Setting
)
from modules.catalog.category.models import Category


class ProductAdmin(admin.ModelAdmin):
    list_display = get_field_list(Product)


class ImageAdmin(admin.ModelAdmin):
    list_display = get_field_list(Image)


class SettingAdmin(admin.ModelAdmin):
    list_display = get_field_list(Setting)


class CategoryAdmin(admin.ModelAdmin):
    list_display = get_field_list(Category)


admin.site.register(Product, ProductAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Setting, SettingAdmin)
admin.site.register(Category, CategoryAdmin)
