# coding=utf-8

"""
Source Base
"""

__all__ = ['BaseViewUpy']

from django.forms import ModelChoiceField
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import Group

from modules.base.models import BaseConfiguration
from modules.company.models import CompanyData, CompanyConfiguration, CompanyRelationship
from modules.catalog.category.models import Category
from modules.customer.models import Customer
from modules.seller.models import Seller


class BaseViewUpy():
    """
    """
    def company_id(self):
        """
        """
        return self.request.session['company_data_id']

    def create_data(self, user):
        """
        """
        try:
            # Create CompanyData
            data = CompanyData(email=user.email)
            data.save()

            # Create Configurations
            params = BaseConfiguration.objects.all()
            
            for config in params:
                configuration = CompanyConfiguration(
                    key=config.key,
                    description=config.description,
                    value=config.value,
                    company_data_id=data.id
                )
                configuration.save()
            
            # Add BasePlan Group
            user_group = Group.objects.get(name='Free')
            user.groups.add(user_group)

            # Add CompanyRelationship
            relationship = CompanyRelationship(company_data_id=data.id,user_id=user.id)
            relationship.save()

            # add Category
            category = Category(
                company_data_id=data.id,
                name=_('Category'),
                code='CAT'
            )
            category.save()

            # add Customer
            customer = Customer(
                company_data_id=data.id,
                first_name=_('Customer'),
                second_name=_('Test'),
                nickname=_('Customer')
            )
            customer.save()

            # add Customer
            seller = Seller(
                company_data_id=data.id,
                first_name=_('Seller'),
                second_name=_('Test'),
                nickname=_('Seller')
            )
            seller.save()

        except:
            raise


class BaseChoiceField(ModelChoiceField):
    """
    """
    def label_from_instance(self, obj):
        return "%s" % obj.id
