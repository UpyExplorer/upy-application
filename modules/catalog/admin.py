from django.contrib import admin
from modules.catalog.product.models import Product, Image, Setting
from modules.catalog.category.models import Category


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id']


class ImageAdmin(admin.ModelAdmin):
    list_display = ['id']


class SettingAdmin(admin.ModelAdmin):
    list_display = ['id']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id']


admin.site.register(Product, ProductAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Setting, SettingAdmin)
admin.site.register(Category, CategoryAdmin)
