from datetime import datetime
from django.db import models
from modules.company.models import Data, Customer, Seller
from modules.base.models import PaymentType
from modules.catalog.product.models import Product


class Payment(models.Model):
    company_data = models.ForeignKey(Data, on_delete=models.SET_NULL, null=True)
    creation_time = models.DateTimeField(default=datetime.now, null=True)
    payment_type = models.CharField(max_length=100,blank=True, null=True)
    operation_type = models.CharField(max_length=100,blank=True, null=True)
    code = models.CharField(max_length=25, blank=False, null=True)
    payment_type = models.ForeignKey(PaymentType, on_delete=models.SET_NULL, null=True)

class Order(models.Model):
    company_data = models.ForeignKey(Data, on_delete=models.SET_NULL, null=True)
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


class Item(models.Model):
    company_data = models.ForeignKey(Data, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(blank=True, null=True)


class ParcelGroup(models.Model):
    company_data = models.ForeignKey(Data, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)


class Parcel(models.Model):
    company_data = models.ForeignKey(Data, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    parcel_group = models.ForeignKey(ParcelGroup, on_delete=models.SET_NULL, null=True)
