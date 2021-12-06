from django.contrib import admin
from modules.sale.models import (
    Payment,
    Order,
    Item,
    ParcelGroup,
    Parcel
)

admin.site.register(Payment)
admin.site.register(Order)
admin.site.register(Item)
admin.site.register(ParcelGroup)
admin.site.register(Parcel)
