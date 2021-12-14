from django.contrib import admin
from modules.base.models import (
    BaseConfiguration,
    BaseModule,
    BasePlan,
    BaseCurrency,
    BaseCategory,
    BasePaymentType,
    BaseCreditOperator
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


admin.site.register(BaseConfiguration, ConfigurationAdmin)
admin.site.register(BaseModule, ModuleAdmin)
admin.site.register(BasePlan, PlanAdmin)
admin.site.register(BaseCurrency, CurrencyAdmin)
admin.site.register(BaseCategory, CategoryAdmin)
admin.site.register(BasePaymentType, PaymentTypeAdmin)
admin.site.register(BaseCreditOperator, CreditOperatorAdmin)
