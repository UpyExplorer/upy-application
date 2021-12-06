
from decimal import Decimal
from django import forms
from django.utils.translation import gettext_lazy as _
from modules.catalog.product.models import Product

class ProductForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        if 'instance' in kwargs:
            kwargs['instance'].price_sell = kwargs['instance'].price_sell.quantize(Decimal('0.00'))
            kwargs['instance'].price_cost = kwargs['instance'].price_cost.quantize(Decimal('0.00'))
            kwargs['instance'].price_promo = kwargs['instance'].price_promo.quantize(Decimal('0.00'))
        super(ProductForm, self).__init__(*args, **kwargs) 
        self.fields['price_sell'].decimal_places = 2
        self.fields['price_cost'].decimal_places = 2
        self.fields['price_promo'].decimal_places = 2

    active = forms.BooleanField(label=_("Active"), required=False)
    name = forms.CharField(label=_("Name"), help_text=_("Maximum 100 characters"))
    sku = forms.CharField(label=_("Sku"), help_text=_("No special characters allowed"))
    type = forms.ChoiceField(label=_("Type"), choices=Product.ITEM_TYPE)
    condition = forms.ChoiceField(label=_("Condition"), choices=Product.ITEM_CONDITION)
    stock = forms.IntegerField(label=_("Stock"), initial=0)
    price_sell = forms.DecimalField(label=_("Price Sell"), initial=0.0, decimal_places=2)
    price_cost = forms.DecimalField(label=_("Price Cost"), initial=0.0, decimal_places=2)
    price_promo = forms.DecimalField(label=_("Price Promo"), initial=0.0, decimal_places=2)
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

