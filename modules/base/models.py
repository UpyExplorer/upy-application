
from datetime import datetime
from django.db import models
from django.contrib.auth.models import Group


class Configuration(models.Model):
    key = models.CharField(max_length=50,blank=True, null=True)
    description = models.CharField(max_length=50,blank=True, null=True)
    value = models.CharField(max_length=10,blank=True, null=True)

class Integration(models.Model):
    code = models.CharField(max_length=20, unique=True)


class Module(models.Model):
    code = models.CharField(max_length=20, unique=True)


class Plan(models.Model):
    code = models.CharField(max_length=20, unique=True)

class Currency(models.Model):
    country_name = models.CharField(max_length=25, blank=False, null=False)
    currency_name = models.CharField(max_length=25, blank=False, null=False)
    code = models.CharField(max_length=5, blank=False, null=False)
    status = models.BooleanField(null=False, default=False)
