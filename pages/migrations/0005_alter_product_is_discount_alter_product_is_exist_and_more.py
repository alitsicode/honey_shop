# Generated by Django 4.2 on 2023-04-06 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_product_properties'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='is_discount',
            field=models.BooleanField(default=False, verbose_name='has_discount'),
        ),
        migrations.AlterField(
            model_name='product',
            name='is_exist',
            field=models.BooleanField(default=True, verbose_name='product_status'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price_with_discount',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='price_with_discount'),
        ),
    ]
