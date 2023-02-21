# coding=utf-8

"""
Module Docstring
"""

from datetime import datetime

from django.db import models
from django.utils.translation import gettext_lazy as _

from modules.company.models import CompanyData
from modules.catalog.product.models import Product


class StockLocale(models.Model):
    company_data = models.ForeignKey(CompanyData, on_delete=models.SET_NULL, null=True)
    creation_time = models.DateTimeField(default=datetime.now, null=True)
    name = models.CharField(max_length=25, blank=False, null=False, default=_('Standard'))
    code = models.CharField(max_length=5, blank=False, null=True, default='STD')
    main = models.BooleanField(null=False, default=False)

    class Meta:
        db_table = 'catalog_stock_locale'
        verbose_name = 'Catalog Stock Locale'
        verbose_name_plural = 'Catalog Stock Locale'


class Stock(models.Model):
    ITEM_TYPE = (
        ('1', _('Other')),
        ('2', _('Input')),
        ('3', _('Exit')),
        ('4', _('Sale')),
        ('5', _('Purchase')),
        ('6', _('Devolution')),
    )

    company_data = models.ForeignKey(CompanyData, on_delete=models.SET_NULL, null=True)
    creation_time = models.DateTimeField(default=datetime.now, null=False)
    type = models.CharField(choices=ITEM_TYPE, max_length=1, default=1, null=False)
    product = models.ForeignKey(Product, related_name='product', on_delete=models.SET_NULL, null=True)
    stock_locale = models.ForeignKey(StockLocale, on_delete=models.SET_NULL, null=True)
    model_class = models.CharField(max_length=15, blank=True, null=True)
    model_id = models.IntegerField(blank=True, null=True)
    quantity = models.IntegerField(null=True)
    new_stock = models.IntegerField(null=True)

    class Meta:
        db_table = 'catalog_stock'
        verbose_name = 'Catalog Stock'
        verbose_name_plural = 'Catalog Stock'
