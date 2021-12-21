from datetime import datetime
from django.db import models
from django import forms
from modules.base.models import ModelUpyBase
from modules.company.models import CompanyData
from modules.catalog.product.models import Product
from modules.application.models import ApplicationLink

def all_application_link():
    objects = ApplicationLink.objects.filter().all()

    options = ()
    for item in objects:
        if not options:
            options = (item.id, item.base_application)
        else:
            options = options, (item.id, item.base_application)

    return options

class AdvertisingLink(forms.Form):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    application_link = forms.ModelChoiceField(queryset=ApplicationLink.objects.filter().all())
    company_data = models.ForeignKey(CompanyData, on_delete=models.SET_NULL, null=True)
    creation_time = models.DateTimeField(default=datetime.now, null=True)
    status = models.BooleanField(null=False, default=False)

    class Meta:
        db_table = 'advertising_link'

