
from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group


class Data(models.Model):
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


class Configuration(models.Model):
    company_data = models.ForeignKey(Data, on_delete=models.SET_NULL, null=True)
    key = models.CharField(max_length=50,blank=True, null=True)
    description = models.CharField(max_length=50,blank=True, null=True)
    value = models.CharField(max_length=10,blank=True, null=True)


class Relationship(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    company_data = models.ForeignKey(Data, on_delete=models.SET_NULL, null=True)
    is_main = models.BooleanField(blank=True, null=True, default=True)


class Customer(models.Model):
    company_data = models.ForeignKey(Data, on_delete=models.SET_NULL, null=True)
    creation_time = models.DateTimeField(default=datetime.now, null=True)
    first_name = models.CharField(max_length=100,blank=True, null=True)
    second_name = models.CharField(max_length=100,blank=True, null=True)
    cpf_cnpj = models.IntegerField(blank=True, null=True)
    nickname = models.CharField(max_length=50,blank=True, null=True)
    email = models.CharField(max_length=100,blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    address_street = models.CharField(max_length=100,blank=True, null=True)
    address_number = models.CharField(max_length=100,blank=True, null=True)
    address_complement = models.CharField(max_length=100,blank=True, null=True)
    address_state = models.CharField(max_length=100,blank=True, null=True)
    address_country = models.CharField(max_length=100,blank=True, null=True)
    address_postal_code = models.IntegerField(blank=True, null=True)
