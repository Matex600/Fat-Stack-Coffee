# Generated by Django 3.2 on 2022-05-10 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fsc_products', '0002_rename_prod_name_product_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='coffee_amounts',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
