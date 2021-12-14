from django.contrib import admin
from modules.company.models import (
    CompanyData,
    CompanyConfiguration,
    CompanyRelationship,
    Customer,
    Seller
)

class CompanyDataAdmin(admin.ModelAdmin):
    list_display = ['id']


class CompanyConfigurationAdmin(admin.ModelAdmin):
    list_display = ['id']


class CompanyRelationshipAdmin(admin.ModelAdmin):
    list_display = ['id']


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id']


class Admin(admin.ModelAdmin):
    list_display = ['id']


class SellerAdmin(admin.ModelAdmin):
    list_display = ['id']


admin.site.register(CompanyData, CompanyDataAdmin)
admin.site.register(CompanyConfiguration, CompanyConfigurationAdmin)
admin.site.register(CompanyRelationship, CompanyRelationshipAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Seller, SellerAdmin)
