
from datetime import datetime
from django.db import models
from modules.company.models import Data


class Data(models.Model):
    company_data = models.ForeignKey(Data, on_delete=models.SET_NULL, null=True)
    created_on = models.DateTimeField(default=datetime.now, null=True)
