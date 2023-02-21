# coding=utf-8

"""
Module Docstring
"""

from django.contrib import admin
from app.utils import get_field_list
from modules.seller.models import (
    Seller
)


class SellerAdmin(admin.ModelAdmin):
    """
    Seller Admin
    """
    list_display = get_field_list(Seller)


admin.site.register(Seller, SellerAdmin)
