# Generated by Django 3.2.9 on 2021-12-13 07:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0016_auto_20211206_0101'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Configuration',
            new_name='BaseConfiguration',
        ),
    ]
