from datetime import datetime
from django.db import models
from modules.base.models import ModelUpyBase
from modules.company.models import CompanyData
from django.utils.translation import gettext_lazy as _


class BaseApplication(ModelUpyBase):
    ITEM_TYPE = (
        ('1', _('Marketplace')),
        ('2', _('E-commerce')),
        ('3', _('Payment')),
        ('4', _('Management')),
        ('5', _('Logistics'))
    )

    name = models.CharField(max_length=100, blank=False, null=False, default='Application')
    code = models.CharField(max_length=25, blank=False, null=True)
    key = models.CharField(max_length=50,blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    url = models.CharField(max_length=100,blank=True, null=True)
    image_name = models.CharField(max_length=50,blank=True, null=True)
    image_url = models.CharField(max_length=100, blank=True, null=True)
    image = models.CharField(max_length=100, blank=True, null=True)
    type = models.CharField(choices=ITEM_TYPE,max_length=1, null=True)
    Installed = models.IntegerField(null=True, default=0)
    stars = models.IntegerField(null=True, default=0)
    status = models.BooleanField(null=False, default=False)

    class Meta:
        db_table = 'base_application'
        verbose_name = 'Base Application'
        verbose_name_plural = 'Base Application'

class ApplicationLink(ModelUpyBase):
    base_application = models.ForeignKey(BaseApplication, on_delete=models.SET_NULL, null=True)
    company_data = models.ForeignKey(CompanyData, on_delete=models.SET_NULL, null=True)
    creation_time = models.DateTimeField(default=datetime.now, null=True)

    class Meta:
        db_table = 'application_link'
        verbose_name = 'Application Link'
        verbose_name_plural = 'Application Link'