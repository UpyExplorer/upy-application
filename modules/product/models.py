
from datetime import datetime
from django.db import models
from modules.company.models import Data


class Info(models.Model):
    company_data = models.ForeignKey(Data, on_delete=models.SET_NULL, null=True)
    creation_time = models.DateTimeField(default=datetime.now, null=True)
