# coding=utf-8

from django.contrib import admin
from app.utils import get_field_list
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
    list_display = get_field_list(BaseConfiguration)


class ModuleAdmin(admin.ModelAdmin):
    list_display = get_field_list(BaseModule)


class PlanAdmin(admin.ModelAdmin):
    list_display = get_field_list(BasePlan)


class CurrencyAdmin(admin.ModelAdmin):
    list_display = get_field_list(BaseCurrency)


class CategoryAdmin(admin.ModelAdmin):
    list_display = get_field_list(BaseCategory)


class PaymentTypeAdmin(admin.ModelAdmin):
    list_display = get_field_list(BasePaymentType)


class CreditOperatorAdmin(admin.ModelAdmin):
    list_display = get_field_list(BaseCreditOperator)


admin.site.register(BaseConfiguration, ConfigurationAdmin)
admin.site.register(BaseModule, ModuleAdmin)
admin.site.register(BasePlan, PlanAdmin)
admin.site.register(BaseCurrency, CurrencyAdmin)
admin.site.register(BaseCategory, CategoryAdmin)
admin.site.register(BasePaymentType, PaymentTypeAdmin)
admin.site.register(BaseCreditOperator, CreditOperatorAdmin)
