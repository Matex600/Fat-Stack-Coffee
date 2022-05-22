# Generated by Django 3.2 on 2022-05-22 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fsc_products', '0007_alter_product_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='rating',
        ),
        migrations.AddField(
            model_name='product',
            name='star_rating',
            field=models.IntegerField(default=2),
        ),
    ]
