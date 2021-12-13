from django.contrib import admin
from modules.base.models import (
    CompanyConfiguration,
    Integration,
    Module,
    Plan,
    Currency,
    Category,
    PaymentType,
    CreditOperator
)

class ConfigurationAdmin(admin.ModelAdmin):
    list_display = ['id', 'key', 'description', 'value']

class IntegrationAdmin(admin.ModelAdmin):
    list_display = ['id', 'code']

class ModuleAdmin(admin.ModelAdmin):
    list_display = ['id', 'key', 'description', 'value', 'url', 'global_permission']

class PlanAdmin(admin.ModelAdmin):
    list_display = ['id', 'code', 'group']

class CurrencyAdmin(admin.ModelAdmin):
    list_display = ['id', 'country_name', 'currency_name', 'code', 'status']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'code']

class PaymentTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'payment_type', 'description', 'code', 'tag', 'currency']


class CreditOperatorAdmin(admin.ModelAdmin):
    list_display = ['id', 'operator_type', 'description', 'code', 'tag', 'currency']

admin.site.register(CompanyConfiguration, ConfigurationAdmin)
admin.site.register(Integration, IntegrationAdmin)
admin.site.register(Module, ModuleAdmin)
admin.site.register(Plan, PlanAdmin)
admin.site.register(Currency, CurrencyAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(PaymentType, PaymentTypeAdmin)
admin.site.register(CreditOperator, CreditOperatorAdmin)
