# Generated by Django 3.2.9 on 2021-12-15 00:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0010_auto_20211213_2308'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seller',
            name='company_data',
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.DeleteModel(
            name='Seller',
        ),
    ]
