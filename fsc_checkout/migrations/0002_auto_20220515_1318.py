# Generated by Django 3.2 on 2022-05-15 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fsc_checkout', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='orderlineitem',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='orderlineitem',
            name='product_weight',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
