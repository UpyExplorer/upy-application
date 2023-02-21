# coding=utf-8

"""
Source Base
"""

__all__ = ['BaseViewUpy']

from django.forms import ModelChoiceField
from django.contrib.auth.models import Group

from modules.base.models import BaseConfiguration
from modules.company.models import CompanyData, CompanyConfiguration, CompanyRelationship
from modules.catalog.category.models import Category
from modules.catalog.stock.models import StockLocale
from modules.customer.models import Customer
from modules.seller.models import Seller


class BaseUpy():
    """
    """
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
                main=True
            )
            category.save()

            # add Customer
            customer = Customer(
                company_data_id=data.id,
                main=True
            )
            customer.save()

            # add Customer
            seller = Seller(
                company_data_id=data.id,
                main=True
            )
            seller.save()

            # add StockLocale
            stock_locale = StockLocale(
                company_data_id=data.id,
                main=True
            )
            stock_locale.save()

        except:
            raise


class BaseViewUpy():
    """
    """
    def company_id(self):
        """
        """
        company_data_id = self.request.session.get('company_data_id')

        if company_data_id:
            return company_data_id
        else:
            company_relation = CompanyRelationship.objects.filter(user=self.request.user.id).first()
            if company_relation:
                return company_relation.company_data

        return None


class BaseChoiceField(ModelChoiceField):
    """
    """
    def label_from_instance(self, obj):
        return "%s" % obj.id
