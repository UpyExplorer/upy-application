from django import forms
from django.utils.translation import gettext_lazy as _

from app.base import BaseChoiceField
from modules.ads.models import AdsLink
from modules.application.models import ApplicationLink
from modules.catalog.product.models import Product


class ChoiceFieldProduct(BaseChoiceField):
    def label_from_instance(self, obj):
        return "%s" % obj.name

class ChoiceFieldApplication(BaseChoiceField):
    def label_from_instance(self, obj):
        return "%s" % obj.base_application.name


class AdsLinkForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        company_data_id = kwargs['instance'].company_data_id

        product = Product.objects.filter(
            company_data=company_data_id
            ).all()

        application_link = ApplicationLink.objects.filter(
            company_data=company_data_id
            ).select_related('base_application').all()

        self.fields['product'] = ChoiceFieldProduct(
            widget=forms.Select,
            queryset=product,
            label=_("Product")
            )

        self.fields['application_link'] = ChoiceFieldApplication(
            widget=forms.Select,
            queryset=application_link,
            label=_("Application")
            )


    class Meta:
        model = AdsLink
        fields = [
            'product',
            'application_link',
            'status'
            ]
        exclude = ['id', 'company_data', 'creation_time']
