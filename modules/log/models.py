
from datetime import datetime
from django.db import models
from modules.company.models import Data


class application_error(models.Model):
    company_data = models.ForeignKey(Data, on_delete=models.SET_NULL, null=True)
    exception_traceback = models.TextField()
    model_type = models.CharField(max_length=25, null=True)
    model_id = models.IntegerField(blank=True, null=True)
    model_content = models.TextField()
    operation = models.CharField(max_length=1, null=True)
    registration_datetime = models.DateTimeField(default=datetime.now, null=True)

class service_error(models.Model):
    company_data = models.ForeignKey(Data, on_delete=models.SET_NULL, null=True)
    exception_traceback = models.TextField()
    model_type = models.CharField(max_length=25, null=True)
    model_id = models.IntegerField(blank=True, null=True)
    model_content = models.TextField()
    operation = models.CharField(max_length=1, null=True)
    registration_datetime = models.DateTimeField(default=datetime.now, null=True)
    
