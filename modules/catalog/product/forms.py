# coding=utf-8

"""
Module Docstring
"""

from decimal import Decimal

from django import forms
from django.utils.translation import gettext_lazy as _

from app.base import BaseChoiceField

from modules.catalog.category.models import Category
from modules.catalog.product.models import Product


class ChoiceFieldCategory(BaseChoiceField):
    def label_from_instance(self, obj):
        return "%s" % obj.name


class ProductForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        """
        """
        try:
            self.request = kwargs.pop('request')
            query_category = Category.objects.filter(
                company_data=self.request.session['company_data_id']
                ).all()

            options = True
        except:
            options = False

        if 'instance' in kwargs:
            if kwargs['instance']:
                kwargs['instance'].price_sell = kwargs['instance'].price_sell.quantize(Decimal('0.00'))
                kwargs['instance'].price_cost = kwargs['instance'].price_cost.quantize(Decimal('0.00'))
                kwargs['instance'].price_promo = kwargs['instance'].price_promo.quantize(Decimal('0.00'))

        super(ProductForm, self).__init__(*args, **kwargs) 
        self.fields['price_sell'].decimal_places = 2
        self.fields['price_cost'].decimal_places = 2
        self.fields['price_promo'].decimal_places = 2

        if options:
            self.fields['category'] = ChoiceFieldCategory(
                widget=forms.Select,
                queryset=query_category,
                label=_("Category")
                )

    class Meta:
        model = Product
        fields = [
            'active',
            'name',
            'category',
            'sku',
            'type',
            'condition',
            'stock',
            'price_sell',
            'price_promo',
            'price_cost',
            'description',
        ]
        exclude = ['creation_time', 'company_data', 'video_url']

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
