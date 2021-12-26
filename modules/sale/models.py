from datetime import datetime

from django.db import models

from modules.base.models import BasePaymentType
from modules.catalog.product.models import Product
from modules.company.models import CompanyData
from modules.customer.models import Customer
from modules.seller.models import Seller


class Payment(models.Model):
    company_data = models.ForeignKey(CompanyData, on_delete=models.SET_NULL, null=True)
    creation_time = models.DateTimeField(default=datetime.now, null=True)
    payment_type = models.CharField(max_length=100,blank=True, null=True)
    operation_type = models.CharField(max_length=100,blank=True, null=True)
    code = models.CharField(max_length=25, blank=False, null=True)
    payment_type = models.ForeignKey(BasePaymentType, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'sale_payment'
        verbose_name = 'Sale Payment'
        verbose_name_plural = 'Sale Payment'


class Order(models.Model):
    company_data = models.ForeignKey(CompanyData, on_delete=models.SET_NULL, null=True)
    creation_time = models.DateTimeField(default=datetime.now, null=True)
    cutomer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    seller = models.ForeignKey(Seller, on_delete=models.SET_NULL, null=True)
    total = models.DecimalField(max_digits=20, decimal_places=5, null=True)
    subtotal = models.DecimalField(max_digits=20, decimal_places=5, null=True)
    status = models.BooleanField(default=False, blank=False, null=True)
    date_created = models.DateTimeField(null=True)
    date_closed = models.DateTimeField(null=True)
    expiration_date = models.DateTimeField(null=True)
    date_last_updated = models.DateTimeField(null=True)

    class Meta:
        db_table = 'sale_order'
        verbose_name = 'Sale Order'
        verbose_name_plural = 'Sale Order'


class Item(models.Model):
    company_data = models.ForeignKey(CompanyData, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'sale_item'
        verbose_name = 'Sale Item'
        verbose_name_plural = 'Sale Item'


class ParcelGroup(models.Model):
    company_data = models.ForeignKey(CompanyData, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'sale_parcel_group'
        verbose_name = 'Sale Parcel Group'
        verbose_name_plural = 'Sale Parcel Group'


class Parcel(models.Model):
    company_data = models.ForeignKey(CompanyData, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    parcel_group = models.ForeignKey(ParcelGroup, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'sale_parcel'
        verbose_name = 'Sale Parcel'
        verbose_name_plural = 'Sale Parcel'
