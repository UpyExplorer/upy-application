
from datetime import datetime
from django.db import models
from django.contrib.auth.models import Group
from global_permissions.models import GlobalPermission


class Configuration(models.Model):
    key = models.CharField(max_length=50,blank=True, null=True)
    description = models.CharField(max_length=50,blank=True, null=True)
    value = models.CharField(max_length=10,blank=True, null=True)

class Integration(models.Model):
    code = models.CharField(max_length=20, unique=True)


class Module(models.Model):
    key = models.CharField(max_length=50,blank=True, null=True)
    description = models.CharField(max_length=50,blank=True, null=True)
    value = models.CharField(max_length=10,blank=True, null=True)
    url = models.CharField(max_length=100,blank=True, null=True)
    global_permission = models.ForeignKey(GlobalPermission, on_delete=models.SET_NULL, null=True)


class Plan(models.Model):
    code = models.CharField(max_length=20, unique=True)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True)

class Currency(models.Model):
    country_name = models.CharField(max_length=25, blank=False, null=False)
    currency_name = models.CharField(max_length=25, blank=False, null=False)
    code = models.CharField(max_length=5, blank=False, null=False)
    status = models.BooleanField(null=False, default=False)

class Category(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False, default='Category')
    code = models.CharField(max_length=25, blank=False, null=True)

class PaymentType(models.Model):
    payment_type = models.CharField(max_length=100,blank=True, null=True)
    operation_type = models.CharField(max_length=100,blank=True, null=True)
    code = models.CharField(max_length=25, blank=False, null=True)