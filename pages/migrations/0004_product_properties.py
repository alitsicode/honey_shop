# Generated by Django 4.2 on 2023-04-06 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_category_short_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='properties',
            field=models.TextField(blank=True, null=True, verbose_name='product_properties'),
        ),
    ]
