
from datetime import datetime
from django.db import models
from modules.company.models import CompanyData
from modules.base.models import Currency
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    company_data = models.ForeignKey(CompanyData, on_delete=models.SET_NULL, null=True)
    creation_time = models.DateTimeField(default=datetime.now, null=True)
    name = models.CharField(max_length=100, blank=False, null=False, default='Category')
    code = models.CharField(max_length=25, blank=False, null=True)

    def get_absolute_url(self):
        return "/catalog/category/{id}".format(id = self.id)
