
from datetime import datetime
from django.db import models
from modules.company.models import Data
from modules.base.models import Currency
from django.utils.translation import gettext_lazy as _

class Product(models.Model):
    ITEM_TYPE = (
        ('1', _('Standard')),
        ('2', _('Variation')),
        ('3', _('Kit')),
    )

    ITEM_CONDITION = (
        ('1', _('New')),
        ('2', _('Used')),
    )

    WARRANTY_OPTION = (
        ('1', _('Seller warranty')),
        ('2', _('Factory warranty')),
        ('2', _('No warranty')),
    )

    WARRANTY_TIME = (
        ('1', _('Days')),
        ('2', _('Months')),
        ('2', _('Years')),
    )

    company_data = models.ForeignKey(Data, on_delete=models.SET_NULL, null=True)
    creation_time = models.DateTimeField(default=datetime.now, null=True)
    name = models.CharField(max_length=100, blank=False, null=False, default='Product')
    subtitle = models.CharField(max_length=100, blank=False, null=False, default='Subtitle')
    description = models.TextField(blank=True, null=True)
    external_code = models.CharField(max_length=25, blank=False, null=True)
    code_ean_gtin = models.CharField(max_length=25, blank=False, null=True)
    code = models.CharField(max_length=25, blank=False, null=True)
    sku = models.CharField(max_length=25, blank=False, null=True)
    price_sell = models.DecimalField(max_digits=20, decimal_places=5, null=True)
    price_cost = models.DecimalField(max_digits=20, decimal_places=5, null=True)
    price_promo = models.DecimalField(max_digits=20, decimal_places=5, null=True)
    detail_weight = models.DecimalField(max_digits=20, decimal_places=5, null=True)
    detail_length = models.DecimalField(max_digits=20, decimal_places=5, null=True)
    detail_width = models.DecimalField(max_digits=20, decimal_places=5, null=True)
    detail_height = models.DecimalField(max_digits=20, decimal_places=5, null=True)
    active = models.BooleanField(null=False, default=False)
    video_url = models.TextField(blank=True, null=True)
    type = models.CharField(choices=ITEM_TYPE,max_length=1, null=True)
    condition = models.CharField(choices=ITEM_CONDITION,max_length=1, null=True)
    stock = models.DecimalField(max_digits=11, decimal_places=7, null=True, default=0)
    sold_quantity = models.IntegerField(null=True, default=0)
    currency = models.ForeignKey(Currency, on_delete=models.SET_NULL, null=True, default=None)
    warranty_option = models.CharField(choices=WARRANTY_OPTION,max_length=1, null=True)
    warranty_time = models.CharField(choices=WARRANTY_TIME,max_length=1, null=True)
    warranty_value = models.IntegerField(null=True, default=0)


    def get_absolute_url(self):
        return "/catalog/product/{id}".format(id = self.id)

    def delete_absolute_url(self):
        return "/catalog/product/delete/{id}".format(id = self.id)


class Image(models.Model):
    ITEM_FORMAT = (
        ('1','JPG'),
        ('2','JPEG'),
        ('3','PNG'),
    )

    company_data = models.ForeignKey(Data, on_delete=models.SET_NULL, null=True)
    creation_time = models.DateTimeField(default=datetime.now, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    original_name = models.CharField(max_length=100, blank=False, null=False)
    fake_name = models.CharField(max_length=100, blank=False, null=False)
    url = models.TextField(blank=True, null=True)
    image_format = models.CharField(choices=ITEM_FORMAT,max_length=1, null=True)
    active = models.BooleanField(null=False, default=False)
    main = models.BooleanField(null=False, default=False)

    def get_absolute_url(self):
        return "/catalog/image/{id}".format(id = self.id)


class Setting(models.Model):
    company_data = models.ForeignKey(Data, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    key = models.CharField(max_length=50,blank=True, null=True)
    description = models.CharField(max_length=50,blank=True, null=True)
    value = models.CharField(max_length=10,blank=True, null=True)
    option_value = models.CharField(max_length=10,blank=True, null=True)