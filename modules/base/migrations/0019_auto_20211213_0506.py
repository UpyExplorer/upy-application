# Generated by Django 3.2.9 on 2021-12-13 08:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0018_delete_integration'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='baseconfiguration',
            table='base_configuration',
        ),
        migrations.AlterModelTable(
            name='category',
            table='base_categorye',
        ),
        migrations.AlterModelTable(
            name='currency',
            table='base_currency',
        ),
        migrations.AlterModelTable(
            name='module',
            table='base_module',
        ),
        migrations.AlterModelTable(
            name='plan',
            table='base_plan',
        ),
    ]
