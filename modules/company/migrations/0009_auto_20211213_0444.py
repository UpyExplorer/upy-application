# Generated by Django 3.2.9 on 2021-12-13 07:44

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('company', '0008_rename_configuration_companyconfiguration'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Relationship',
            new_name='CompanyRelationship',
        ),
        migrations.AlterModelTable(
            name='companyrelationship',
            table='company_relationship',
        ),
    ]
