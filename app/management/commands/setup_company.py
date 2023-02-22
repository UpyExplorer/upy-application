from django.core import management
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group

from modules.base.models import BaseConfiguration
from modules.company.models import (
    CompanyData,
    CompanyConfiguration,
    CompanyRelationship
)
from modules.catalog.category.models import Category
from modules.catalog.stock.models import StockLocale
from modules.customer.models import Customer


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('user_id', nargs='+', type=int)

    def handle(self, *args, **options):
        user = User.objects.get(id=options.get('user_id')[0])
        
        if not CompanyData.objects.filter(email=user.email):
            company_data = CompanyData(email=user.email)
            company_data.save()

            # Create Configurations
            params = BaseConfiguration.objects.all()

            for config in params:
                configuration = CompanyConfiguration(
                    key=config.key,
                    description=config.description,
                    value=config.value,
                    company_data_id=company_data.id
                )
                configuration.save()

            # Add BasePlan Group
            user_group = Group.objects.get(name='Plan - Free')
            user.groups.add(user_group)
            user.save()

            # Add CompanyRelationship
            relationship = CompanyRelationship(
                company_data_id=company_data.id, user_id=user.id)
            relationship.save()

            # add Category
            category = Category(
                company_data_id=company_data.id,
                main=True)
            category.save()

            # add StockLocale
            stock_locale = StockLocale(
                company_data_id=company_data.id,
                main=True)
            stock_locale.save()
