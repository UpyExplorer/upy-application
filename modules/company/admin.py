from django.contrib import admin
from modules.company.models import (
    CompanyData,
    CompanyConfiguration,
    CompanyRelationship,
    Customer,
    Seller
)

admin.site.register(CompanyData)
admin.site.register(CompanyConfiguration)
admin.site.register(CompanyRelationship)
admin.site.register(Customer)
admin.site.register(Seller)
