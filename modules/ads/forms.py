
from decimal import Decimal
from django import forms
from django.forms import fields
from django.forms.forms import Form
from django.utils.translation import gettext_lazy as _
from modules.catalog.product.models import Product
from modules.ads.models import AdsLink


class AdsLinkForm(forms.ModelForm):
    product = forms.ModelChoiceField(
        widget=forms.Select,
        queryset=Product.objects.all()
        )
   
    class Meta:
        model = AdsLink
        fields = [
            'product',
            'application_link',
            'creation_time',
            'status'
            ]
        exclude = ['id', 'company_data']
