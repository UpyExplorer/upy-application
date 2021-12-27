# Generated by Django 3.2.9 on 2021-12-27 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0027_alter_stocklocale_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='main',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='category',
            name='code',
            field=models.CharField(default='CAT', max_length=25, null=True),
        ),
    ]
