# Generated by Django 3.2.9 on 2021-12-27 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0021_auto_20211227_0053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='model_class',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='model_id',
            field=models.IntegerField(null=True),
        ),
    ]
