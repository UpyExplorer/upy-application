# Generated by Django 3.2.9 on 2021-11-22 08:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_globalparam'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='GlobalParam',
            new_name='Param',
        ),
    ]
