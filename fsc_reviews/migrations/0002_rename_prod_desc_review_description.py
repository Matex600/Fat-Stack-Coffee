# Generated by Django 3.2 on 2022-05-20 20:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fsc_reviews', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='prod_desc',
            new_name='description',
        ),
    ]
