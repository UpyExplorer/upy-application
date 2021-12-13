from django.db import models
from modules.base.models import ModelUpyBase

class BaseApplication(ModelUpyBase):
    name = models.CharField(max_length=100, blank=False, null=False, default='Application')
    code = models.CharField(max_length=25, blank=False, null=True)
    key = models.CharField(max_length=50,blank=True, null=True)
    description = models.CharField(max_length=50,blank=True, null=True)
    url = models.CharField(max_length=100,blank=True, null=True)

    class Meta:
        db_table = 'base_application'

class ApplicationLink(ModelUpyBase):
    code = models.CharField(max_length=25, blank=False, null=True)

    class Meta:
        db_table = 'application_link'