from django.contrib import admin
from modules.company.models import (
    Data,
    Configuration,
    Relationship,
    Customer,
    Seller
)

admin.site.register(Data)
admin.site.register(Configuration)
admin.site.register(Relationship)
admin.site.register(Customer)
admin.site.register(Seller)
