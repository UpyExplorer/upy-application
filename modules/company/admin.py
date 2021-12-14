from django.contrib import admin
from app.base import get_field_list
from modules.company.models import (
    CompanyData,
    CompanyConfiguration,
    CompanyRelationship,
    Customer,
    Seller
)

class CompanyDataAdmin(admin.ModelAdmin):
    list_display = get_field_list(CompanyData)


class CompanyConfigurationAdmin(admin.ModelAdmin):
    list_display = get_field_list(CompanyConfiguration)


class CompanyRelationshipAdmin(admin.ModelAdmin):
    list_display = get_field_list(CompanyRelationship)


class CustomerAdmin(admin.ModelAdmin):
    list_display = get_field_list(Customer)


class SellerAdmin(admin.ModelAdmin):
    list_display = get_field_list(Seller)


admin.site.register(CompanyData, CompanyDataAdmin)
admin.site.register(CompanyConfiguration, CompanyConfigurationAdmin)
admin.site.register(CompanyRelationship, CompanyRelationshipAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Seller, SellerAdmin)
