
from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from modules.base.models import ModelUpyBase


class CompanyData(ModelUpyBase):
    plan = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, default=1)
    corporate_name = models.CharField(max_length=100,blank=True, null=True)
    corporate_code = models.IntegerField(blank=True, null=True)
    email = models.EmailField(blank=False, null=False)
    active = models.BooleanField(default=False, blank=False, null=True)
    registration_date = models.DateTimeField(default=datetime.now, null=True)
    fantasy_name = models.CharField(max_length=100,blank=True, null=True)
    opening_date = models.DateField(blank=True, null=True)
    postage = models.CharField(max_length=100,blank=True, null=True)
    legal_nature = models.CharField(max_length=100,blank=True, null=True)
    option_by_mei = models.BooleanField(blank=True, null=True)
    option_for_simple = models.BooleanField(blank=True, null=True)
    simple_datao_ption = models.DateField(blank=True, null=True)
    share_capital = models.FloatField(default=0.0,blank=True, null=True)
    type = models.CharField(max_length=25,blank=True, null=True)
    situation = models.DateField(blank=True, null=True)
    data_registration_status = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'company_data'
        verbose_name = 'Company Data'
        verbose_name_plural = 'Company Data'


class CompanyConfiguration(models.Model):
    company_data = models.ForeignKey(CompanyData, on_delete=models.SET_NULL, null=True)
    key = models.CharField(max_length=50,blank=True, null=True)
    description = models.CharField(max_length=50,blank=True, null=True)
    value = models.CharField(max_length=10,blank=True, null=True)

    class Meta:
        db_table = 'company_configuration'
        verbose_name = 'Company Configuration'
        verbose_name_plural = 'Company Configuration'


class CompanyRelationship(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    company_data = models.ForeignKey(CompanyData, on_delete=models.SET_NULL, null=True)
    is_main = models.BooleanField(blank=True, null=True, default=True)

    class Meta:
        db_table = 'company_relationship'
        verbose_name = 'Company Relationship'
        verbose_name_plural = 'Company Relationship'
