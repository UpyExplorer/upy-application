
from datetime import datetime
from django.db import models
from modules.company.models import Data


class Product(models.Model):
    company_data = models.ForeignKey(Data, on_delete=models.SET_NULL, null=True)
    creation_time = models.DateTimeField(default=datetime.now, null=True)
    name = models.CharField(max_length=100, blank=False, null=False, default='Product')
    description = models.TextField(blank=True, null=True)
    external_code = models.CharField(max_length=25, blank=False, null=True)
    code_ean_gtin = models.CharField(max_length=25, blank=False, null=True)
    code = models.CharField(max_length=25, blank=False, null=True)
    sku = models.CharField(max_length=25, blank=False, null=True)
    price_sell = models.DecimalField(max_digits=11, decimal_places=7, null=True)
    price_cost = models.DecimalField(max_digits=11, decimal_places=7, null=True)
    price_promo = models.DecimalField(max_digits=11, decimal_places=7, null=True)
    detail_weight = models.DecimalField(max_digits=8, decimal_places=5, null=True)
    detail_length = models.DecimalField(max_digits=8, decimal_places=5, null=True)
    detail_width = models.DecimalField(max_digits=8, decimal_places=5, null=True)
    detail_height = models.DecimalField(max_digits=8, decimal_places=5, null=True)
    active = models.BooleanField(null=False, default=False)
    video_url = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=25, blank=False, null=True)
    stock = models.DecimalField(max_digits=11, decimal_places=7, null=True, default=0)

    def get_absolute_url(self):
        return "/catalog/product/{id}".format(id = self.id)
