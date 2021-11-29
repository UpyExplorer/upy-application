from django import forms
from modules.catalog.product.models import Product

class ProductForm(forms.ModelForm):
    name = forms.CharField(help_text="Product name")
    sku = forms.CharField(help_text="Sku")

    class Meta:
        model = Product
        exclude = ['creation_time', 'company_data', 'video_url']

# class ProductForm(forms.Form):
#     name = forms.CharField(help_text="Product name")
#     sku = forms.CharField(help_text="Sku")

