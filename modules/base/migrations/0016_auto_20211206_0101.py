# Generated by Django 3.2.9 on 2021-12-06 04:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0015_auto_20211206_0100'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='creditoperator',
            table='base_credit_operator',
        ),
        migrations.AlterModelTable(
            name='paymenttype',
            table='base_payment_type',
        ),
    ]
