from django.contrib import admin
from app.base import get_field_list
from modules.seller.models import (
    Seller
)

class SellerAdmin(admin.ModelAdmin):
    list_display = get_field_list(Seller)


admin.site.register(Seller, SellerAdmin)
