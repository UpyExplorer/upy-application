# Generated by Django 3.2.9 on 2021-11-28 01:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_rename_created_datetime_info_created_on'),
    ]

    operations = [
        migrations.RenameField(
            model_name='info',
            old_name='created_on',
            new_name='creation_time',
        ),
    ]
