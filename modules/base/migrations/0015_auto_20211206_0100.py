# Generated by Django 3.2.9 on 2021-12-06 04:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_auto_20211206_0054'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymenttype',
            name='tag',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.CreateModel(
            name='CreditOperator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operator_type', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
                ('code', models.CharField(max_length=25, null=True)),
                ('tag', models.CharField(blank=True, max_length=10, null=True)),
                ('currency', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.currency')),
            ],
            options={
                'db_table': 'credit_operator',
            },
        ),
    ]