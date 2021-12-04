from django import forms
from django.utils.translation import gettext_lazy as _
from modules.catalog.product.models import Product

class ProductForm(forms.ModelForm):
    active = forms.BooleanField(label=_("Active"))
    name = forms.CharField(label=_("Name"), help_text=_("Maximum 100 characters"))
    sku = forms.CharField(label=_("Sku"), help_text=_("No special characters allowed"))
    type = forms.ChoiceField(label=_("Type"), choices=Product.ITEM_TYPE)
    stock = forms.IntegerField(label=_("Stock"))
    price_sell = forms.DecimalField(label=_("Price Sell"))
    price_cost = forms.DecimalField(label=_("Price Cost"))
    price_promo = forms.DecimalField(label=_("Price Promo"))
    description = forms.CharField(
        label=_("Description"),
        widget=forms.Textarea,
        max_length=500,
        help_text=_("Maximum 500 characters")
    )

    class Meta:
        model = Product
        fields = ['active','name', 'sku', 'type', 'stock', 'price_sell', 'price_cost', 'price_promo', 'description']
        exclude = ['creation_time', 'company_data', 'video_url']

