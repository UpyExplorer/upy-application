# Generated by Django 3.2.9 on 2021-12-13 08:41

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0009_auto_20211213_0444'),
        ('application', '0003_auto_20211213_0454'),
        ('catalog', '0014_alter_product_stock'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdvertisingLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_time', models.DateTimeField(default=datetime.datetime.now, null=True)),
                ('application_link', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='application.applicationlink')),
                ('company_data', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='company.companydata')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.product')),
            ],
            options={
                'db_table': 'advertising_link',
            },
        ),
    ]