# coding=utf-8

"""
Model Config
"""

from datetime import datetime

from django.db import models

from modules.application.models import ApplicationLink
from modules.base.models import ModelUpyBase
from modules.catalog.product.models import Product
from modules.company.models import CompanyData


class AdsLink(ModelUpyBase):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    application_link = models.ForeignKey(ApplicationLink, on_delete=models.SET_NULL, null=True)
    company_data = models.ForeignKey(CompanyData, on_delete=models.SET_NULL, null=True)
    creation_time = models.DateTimeField(default=datetime.now, null=True)
    status = models.BooleanField(null=False, default=False)
    external_id = models.CharField(max_length=50, blank=True, null=True, db_index=True)

    class Meta:
        db_table = 'ads_link'
        verbose_name = 'Ads Link'
        verbose_name_plural = 'Ads Link'

    def get_absolute_url(self):
        return "/ads/{id}".format(id=self.id)
