# Generated by Django 3.2 on 2022-05-22 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fsc_products', '0008_auto_20220522_0906'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='number_of_ratings',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='rating_sum',
            field=models.IntegerField(default=0),
        ),
    ]