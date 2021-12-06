
from datetime import datetime
from django.db import models
from django.contrib.auth.models import Group
from global_permissions.models import GlobalPermission


class ModelUpyBase(models.Model):

    def get_queryset(self, request):
        return super().get_queryset(request).using(self.using)
 
    class Meta:
        abstract = True

class Configuration(ModelUpyBase):
    key = models.CharField(max_length=50,blank=True, null=True)
    description = models.CharField(max_length=50,blank=True, null=True)
    value = models.CharField(max_length=10,blank=True, null=True)


class Integration(ModelUpyBase):
    code = models.CharField(max_length=20, unique=True)


class Module(ModelUpyBase):
    key = models.CharField(max_length=50,blank=True, null=True)
    description = models.CharField(max_length=50,blank=True, null=True)
    value = models.CharField(max_length=10,blank=True, null=True)
    url = models.CharField(max_length=100,blank=True, null=True)
    global_permission = models.ForeignKey(GlobalPermission, on_delete=models.SET_NULL, null=True)


class Plan(ModelUpyBase):
    code = models.CharField(max_length=20, unique=True)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True)

class Currency(ModelUpyBase):
    country_name = models.CharField(max_length=25, blank=False, null=False)
    currency_name = models.CharField(max_length=25, blank=False, null=False)
    code = models.CharField(max_length=5, blank=False, null=False)
    status = models.BooleanField(null=False, default=False)

class Category(ModelUpyBase):
    name = models.CharField(max_length=100, blank=False, null=False, default='Category')
    code = models.CharField(max_length=25, blank=False, null=True)

class PaymentType(ModelUpyBase):
    payment_type = models.CharField(max_length=50,blank=True, null=True)
    operation_type = models.CharField(max_length=50,blank=True, null=True)
    description = models.CharField(max_length=100,blank=True, null=True)
    code = models.CharField(max_length=25, blank=False, null=True)
    currency = models.ForeignKey(Currency, on_delete=models.SET_NULL, null=True)
    tag = models.CharField(max_length=10,blank=True, null=True)

    class Meta:
        db_table = 'base_payment_type'

class CreditOperator(ModelUpyBase):
    operator_type = models.CharField(max_length=50,blank=True, null=True)
    description = models.CharField(max_length=100,blank=True, null=True)
    code = models.CharField(max_length=25, blank=False, null=True)
    currency = models.ForeignKey(Currency, on_delete=models.SET_NULL, null=True)
    tag = models.CharField(max_length=10,blank=True, null=True)

    class Meta:
        db_table = 'base_credit_operator'