from django import forms
from django.utils.translation import gettext_lazy as _
from modules.catalog.product.models import Product

class ProductForm(forms.ModelForm):
    active = forms.BooleanField(label=_("Active"), required=False)
    name = forms.CharField(label=_("Name"), help_text=_("Maximum 100 characters"))
    sku = forms.CharField(label=_("Sku"), help_text=_("No special characters allowed"))
    type = forms.ChoiceField(label=_("Type"), choices=Product.ITEM_TYPE)
    condition = forms.ChoiceField(label=_("Condition"), choices=Product.ITEM_CONDITION)
    stock = forms.IntegerField(label=_("Stock"), initial=0)
    price_sell = forms.DecimalField(label=_("Price Sell"), initial=0.0)
    price_cost = forms.DecimalField(label=_("Price Cost"), initial=0.0)
    price_promo = forms.DecimalField(label=_("Price Promo"), initial=0.0)
    description = forms.CharField(
        label=_("Description"),
        widget=forms.Textarea,
        max_length=500,
        required=False,
        help_text=_("Maximum 500 characters")
    )

    class Meta:
        model = Product
        fields = [
            'active',
            'name',
            'sku',
            'type',
            'condition',
            'stock',
            'price_sell',
            'price_cost',
            'price_promo',
            'description',
        ]
        exclude = ['creation_time', 'company_data', 'video_url']

