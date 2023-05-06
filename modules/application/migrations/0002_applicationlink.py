# Generated by Django 3.2.9 on 2021-12-13 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=25, null=True)),
            ],
            options={
                'db_table': 'application_link',
            },
        ),
    ]