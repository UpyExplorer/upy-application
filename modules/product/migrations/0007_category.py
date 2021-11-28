# Generated by Django 3.2.9 on 2021-11-28 02:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_info', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.info')),
            ],
        ),
    ]
