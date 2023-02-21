# coding=utf-8

"""
Model Config
"""

from django.db import models
from django.contrib.auth.models import Group

from global_permissions.models import GlobalPermission


class ModelUpyBase(models.Model):

    def get_queryset(self, request):
        return super().get_queryset(request).using(self.using)
 
    class Meta:
        abstract = True


class BaseConfiguration(ModelUpyBase):
    key = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=50, blank=True, null=True)
    value = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        db_table = 'base_configuration'
        verbose_name = 'Base Configuration'
        verbose_name_plural = 'Base Configuration'


class BaseModule(ModelUpyBase):
    key = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=50, blank=True, null=True)
    value = models.CharField(max_length=10, blank=True, null=True)
    url = models.CharField(max_length=100, blank=True, null=True)
    global_permission = models.ForeignKey(GlobalPermission, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'base_module'
        verbose_name = 'Base Module'
        verbose_name_plural = 'Base Module'


class BasePlan(ModelUpyBase):
    code = models.CharField(max_length=20, unique=True)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'base_plan'
        verbose_name = 'Base Plan'
        verbose_name_plural = 'Base Plan'


class BaseCurrency(ModelUpyBase):
    country_name = models.CharField(max_length=25, blank=False, null=False)
    currency_name = models.CharField(max_length=25, blank=False, null=False)
    code = models.CharField(max_length=5, blank=False, null=False)
    status = models.BooleanField(null=False, default=False)

    class Meta:
        db_table = 'base_currency'
        verbose_name = 'Base Currency'
        verbose_name_plural = 'Base Currency'


class BaseCategory(ModelUpyBase):
    name = models.CharField(max_length=100, blank=False, null=False, default='BaseCategory')
    code = models.CharField(max_length=25, blank=False, null=True)

    class Meta:
        db_table = 'base_category'
        verbose_name = 'Base Category'
        verbose_name_plural = 'Base Category'


class BasePaymentType(ModelUpyBase):
    payment_type = models.CharField(max_length=50, blank=True, null=True)
    operation_type = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    code = models.CharField(max_length=25, blank=False, null=True)
    currency = models.ForeignKey(BaseCurrency, on_delete=models.SET_NULL, null=True)
    tag = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        db_table = 'base_payment_type'
        verbose_name = 'Base Payment Type'
        verbose_name_plural = 'Base Payment Type'


class BaseCreditOperator(ModelUpyBase):
    operator_type = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    code = models.CharField(max_length=25, blank=False, null=True)
    currency = models.ForeignKey(BaseCurrency, on_delete=models.SET_NULL, null=True)
    tag = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        db_table = 'base_credit_operator'
        verbose_name = 'Base Credit Operator'
        verbose_name_plural = 'Base Credit Operator'
