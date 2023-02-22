from django.core import management
from django.core.management.base import BaseCommand
from django.core.management.commands import migrate, loaddata


class Command(BaseCommand):

    fixtures = [
        'auth_group.json',
        'auth_user.json',
        'auth_user_groups.json',
        'base_application.json',
        'base_category.json',
        'base_configuration.json',
        'base_currency.json',
        'base_payment_type.json',
        'company_data.json',
        'company_relationship.json'
    ]

    def handle(self, *args, **options):
        management.call_command(migrate.Command())
        for item in self.fixtures:
            management.call_command(loaddata.Command(), item, verbosity=0)
