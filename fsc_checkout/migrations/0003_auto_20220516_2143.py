# Generated by Django 3.2 on 2022-05-16 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fsc_checkout', '0002_auto_20220515_1318'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='original_cart',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='order',
            name='stripe_pid',
            field=models.CharField(default='', max_length=254),
        ),
    ]
