from datetime import datetime
from django.db import models
from modules.base.models import ModelUpyBase
from modules.company.models import CompanyData
from modules.catalog.product.models import Product
from modules.application.models import ApplicationLink

class AdvertisingLink(ModelUpyBase):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    application_link = models.ForeignKey(ApplicationLink, on_delete=models.SET_NULL, null=True)
    company_data = models.ForeignKey(CompanyData, on_delete=models.SET_NULL, null=True)
    creation_time = models.DateTimeField(default=datetime.now, null=True)

    class Meta:
        db_table = 'advertising_link'
        verbose_name = 'Advertising Link'
        verbose_name_plural = 'Advertising Link'