# coding=utf-8

"""
Model Config
"""

from datetime import datetime

from django.db import models
from django.utils.translation import gettext_lazy as _

from modules.base.models import ModelUpyBase
from modules.company.models import CompanyData


class Seller(ModelUpyBase):
    """
    Seller
    """

    company_data = models.ForeignKey(CompanyData, on_delete=models.SET_NULL, null=True)
    creation_time = models.DateTimeField(default=datetime.now, null=True)
    first_name = models.CharField(max_length=100, blank=True, null=True, default=_('Seller'))
    second_name = models.CharField(max_length=100, blank=True, null=True, default=_('Test'))
    cpf_cnpj = models.IntegerField(blank=True, null=True)
    nickname = models.CharField(max_length=50, blank=True, null=True, default=_('Seller'))
    email = models.CharField(max_length=100, blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    address_street = models.CharField(max_length=100, blank=True, null=True)
    address_number = models.CharField(max_length=100, blank=True, null=True)
    address_complement = models.CharField(max_length=100, blank=True, null=True)
    address_state = models.CharField(max_length=100, blank=True, null=True)
    address_country = models.CharField(max_length=100, blank=True, null=True)
    address_postal_code = models.IntegerField(blank=True, null=True)
    main = models.BooleanField(null=False, default=False)

    class Meta:
        """
        Meta
        """
        db_table = 'seller'
        verbose_name = 'Seller'
        verbose_name_plural = 'Seller'
