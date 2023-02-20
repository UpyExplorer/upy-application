# coding=utf-8

"""
Model Config
"""

from datetime import datetime

from django.db import models
from django.utils.translation import gettext_lazy as _

from modules.company.models import CompanyData


class Category(models.Model):
    company_data = models.ForeignKey(CompanyData, on_delete=models.SET_NULL, null=True)
    creation_time = models.DateTimeField(default=datetime.now, null=True)
    name = models.CharField(max_length=100, blank=False, null=False, default=_('Category'))
    code = models.CharField(max_length=25, blank=False, null=True, default='CAT')
    main = models.BooleanField(null=False, default=False)

    class Meta:
        verbose_name = 'Catalog Category'
        verbose_name_plural = 'Catalog Category'


    def get_absolute_url(self):
        return "/catalog/category/{id}".format(id = self.id)
