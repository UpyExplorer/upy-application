# Generated by Django 3.2.9 on 2021-12-27 04:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0024_stock_main'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='main',
        ),
    ]
