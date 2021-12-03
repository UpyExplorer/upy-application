from django import forms
from django.utils.translation import gettext_lazy as _
from modules.catalog.product.models import Product

class ProductForm(forms.ModelForm):
    name = forms.CharField(help_text=_("Maximum 100 characters"))
    sku = forms.CharField(help_text=_("No special characters allowed"))
    price_sell = forms.DecimalField()
    price_cost = forms.DecimalField()
    price_promo = forms.DecimalField()

    class Meta:
        model = Product
        fields = ['name', 'sku', 'type', 'stock', 'price_sell', 'price_cost', 'price_promo', 'description']
        exclude = ['creation_time', 'company_data', 'video_url']

