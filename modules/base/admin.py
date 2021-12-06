from django.contrib import admin
from modules.base.models import (
    Configuration,
    Integration,
    Module,
    Plan,
    Currency,
    Category,
    PaymentType
)

class ConfigurationAdmin(admin.ModelAdmin):
    list_display = ['key', 'description', 'value']

class IntegrationAdmin(admin.ModelAdmin):
    list_display = ['code']

class ModuleAdmin(admin.ModelAdmin):
    list_display = ['key', 'description', 'value', 'url', 'global_permission']

class PlanAdmin(admin.ModelAdmin):
    list_display = ['code', 'group']

class CurrencyAdmin(admin.ModelAdmin):
    list_display = ['country_name', 'currency_name', 'code', 'status']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'code']

class PaymentTypeAdmin(admin.ModelAdmin):
    list_display = ['payment_type', 'operation_type', 'code']

admin.site.register(Configuration, ConfigurationAdmin)
admin.site.register(Integration, IntegrationAdmin)
admin.site.register(Module, ModuleAdmin)
admin.site.register(Plan, PlanAdmin)
admin.site.register(Currency, CurrencyAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(PaymentType, PaymentTypeAdmin)