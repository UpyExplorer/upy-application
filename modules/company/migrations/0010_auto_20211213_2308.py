# Generated by Django 3.2.9 on 2021-12-14 02:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0009_auto_20211213_0444'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='companyconfiguration',
            options={'verbose_name': 'Company Configuration', 'verbose_name_plural': 'Company Configuration'},
        ),
        migrations.AlterModelOptions(
            name='companydata',
            options={'verbose_name': 'Company Data', 'verbose_name_plural': 'Company Data'},
        ),
        migrations.AlterModelOptions(
            name='companyrelationship',
            options={'verbose_name': 'Company Relationship', 'verbose_name_plural': 'Company Relationship'},
        ),
        migrations.AlterModelOptions(
            name='customer',
            options={'verbose_name': 'Customer', 'verbose_name_plural': 'Customer'},
        ),
        migrations.AlterModelOptions(
            name='seller',
            options={'verbose_name': 'Seller', 'verbose_name_plural': 'Seller'},
        ),
    ]
