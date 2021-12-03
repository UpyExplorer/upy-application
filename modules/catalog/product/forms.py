from django import forms
from django.utils.translation import gettext_lazy as _
from modules.catalog.product.models import Product

class ProductForm(forms.ModelForm):
    active = forms.BooleanField(label=_("Active"))
    name = forms.CharField(label=_("Nome"), help_text=_("Maximum 100 characters"))
    sku = forms.CharField(label=_("Sku"), help_text=_("No special characters allowed"))
    type = forms.ChoiceField(label=_("Tipo"), choices=Product.ITEM_TYPE)
    stock = forms.IntegerField(label=_("Estoque"))
    price_sell = forms.DecimalField(label=_("Preço de Venda"))
    price_cost = forms.DecimalField(label=_("Preço de Custo"))
    price_promo = forms.DecimalField(label=_("Preço Promocional"))
    description = forms.CharField(label=_("Descrição"))

    class Meta:
        model = Product
        fields = ['active','name', 'sku', 'type', 'stock', 'price_sell', 'price_cost', 'price_promo', 'description']
        exclude = ['creation_time', 'company_data', 'video_url']

