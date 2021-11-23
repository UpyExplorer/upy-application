# Generated by Django 3.2.9 on 2021-11-22 00:11

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Configuration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.CharField(blank=True, max_length=50, null=True)),
                ('value', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('corporate_name', models.CharField(blank=True, max_length=100, null=True)),
                ('corporate_code', models.IntegerField(blank=True, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('active', models.BooleanField(default=False, null=True)),
                ('registration_date', models.DateTimeField(default=datetime.datetime.now, null=True)),
                ('fantasy_name', models.CharField(blank=True, max_length=100, null=True)),
                ('opening_date', models.DateField(blank=True, null=True)),
                ('postage', models.CharField(blank=True, max_length=100, null=True)),
                ('legal_nature', models.CharField(blank=True, max_length=100, null=True)),
                ('option_by_mei', models.BooleanField(blank=True, null=True)),
                ('option_for_simple', models.BooleanField(blank=True, null=True)),
                ('simple_datao_ption', models.DateField(blank=True, null=True)),
                ('share_capital', models.FloatField(blank=True, default=0.0, null=True)),
                ('type', models.CharField(blank=True, max_length=25, null=True)),
                ('situation', models.DateField(blank=True, null=True)),
                ('data_registration_status', models.DateField(blank=True, null=True)),
                ('plan', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='auth.group')),
            ],
        ),
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_main', models.BooleanField(blank=True, default=True, null=True)),
                ('data', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='company.data')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]