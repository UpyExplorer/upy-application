from django.contrib import admin
from app.base import get_field_list
from modules.sale.models import (
    Payment,
    Order,
    Item,
    ParcelGroup,
    Parcel
)


class PaymentAdmin(admin.ModelAdmin):
    list_display = get_field_list(Payment)


class OrderAdmin(admin.ModelAdmin):
    list_display = get_field_list(Order)


class ItemAdmin(admin.ModelAdmin):
    list_display = get_field_list(Item)


class ParcelGroupAdmin(admin.ModelAdmin):
    list_display = get_field_list(ParcelGroup)


class ParcelAdmin(admin.ModelAdmin):
    list_display = get_field_list(Parcel)


admin.site.register(Payment, PaymentAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(ParcelGroup, ParcelGroupAdmin)
admin.site.register(Parcel, ParcelAdmin)
