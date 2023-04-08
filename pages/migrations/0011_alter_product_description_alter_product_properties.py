# Generated by Django 4.2 on 2023-04-08 14:35

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0010_gallery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=ckeditor.fields.RichTextField(verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='product',
            name='properties',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='product_properties'),
        ),
    ]
