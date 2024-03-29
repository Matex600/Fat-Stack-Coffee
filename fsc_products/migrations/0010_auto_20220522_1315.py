# Generated by Django 3.2 on 2022-05-22 13:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fsc_users', '0001_initial'),
        ('fsc_products', '0009_auto_20220522_0936'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='number_of_ratings',
        ),
        migrations.RemoveField(
            model_name='product',
            name='rating_sum',
        ),
        migrations.RemoveField(
            model_name='product',
            name='star_rating',
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=450)),
                ('star_rating', models.IntegerField()),
                ('review_time', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='fsc_products.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='fsc_users.userprofile')),
            ],
        ),
    ]
