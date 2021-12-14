from datetime import datetime
from django.db import models
from modules.base.models import ModelUpyBase
from modules.company.models import CompanyData

class BaseApplication(ModelUpyBase):
    name = models.CharField(max_length=100, blank=False, null=False, default='Application')
    code = models.CharField(max_length=25, blank=False, null=True)
    key = models.CharField(max_length=50,blank=True, null=True)
    description = models.CharField(max_length=50,blank=True, null=True)
    url = models.CharField(max_length=100,blank=True, null=True)

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