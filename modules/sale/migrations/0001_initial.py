# Generated by Django 3.2.9 on 2021-12-06 01:03

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catalog', '0014_alter_product_stock'),
        ('company', '0005_seller'),
        ('base', '0008_plan_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_time', models.DateTimeField(default=datetime.datetime.now, null=True)),
                ('total', models.DecimalField(decimal_places=5, max_digits=20, null=True)),
                ('subtotal', models.DecimalField(decimal_places=5, max_digits=20, null=True)),
                ('status', models.BooleanField(default=False, null=True)),
                ('date_created', models.DateTimeField(null=True)),
                ('date_closed', models.DateTimeField(null=True)),
                ('expiration_date', models.DateTimeField(null=True)),
                ('date_last_updated', models.DateTimeField(null=True)),
                ('company_data', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='company.data')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_time', models.DateTimeField(default=datetime.datetime.now, null=True)),
                ('operation_type', models.CharField(blank=True, max_length=100, null=True)),
                ('code', models.CharField(max_length=25, null=True)),
                ('company_data', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='company.data')),
                ('payment_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.paymenttype')),
            ],
        ),
        migrations.CreateModel(
            name='ParcelGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_data', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='company.data')),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sale.order')),
            ],
        ),
        migrations.CreateModel(
            name='Parcel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_data', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='company.data')),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sale.order')),
                ('parcel_group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sale.parcelgroup')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('company_data', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='company.data')),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sale.order')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.product')),
            ],
        ),
    ]
