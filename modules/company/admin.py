from django.contrib import admin
from modules.company.models import (
    CompanyData,
    Configuration,
    Relationship,
    Customer,
    Seller
)

admin.site.register(CompanyData)
admin.site.register(Configuration)
admin.site.register(Relationship)
admin.site.register(Customer)
admin.site.register(Seller)
