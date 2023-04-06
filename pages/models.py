from django.db import models
from django.views import generic
from accounts.models import Customeuser
from django.utils.translation import gettext_lazy as _
from django.utils.html import format_html
# Create your models here.

class Category(models.Model):
    title=models.CharField(_("title"), max_length=100)
    short_description=models.TextField(_("description"),default='description')
    image=models.ImageField(_("image"), upload_to='category_image')
    created=models.DateTimeField(_("created time"), auto_now_add=True)
    updated=models.DateTimeField(_("updated time"), auto_now=True)
    
    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.title

    def image_tag(self):
        return format_html('<img width=100px height=100px src="{}" />'. format(self.image.url))


class Product(models.Model):
    title=models.CharField(_("title"), max_length=50)
    description=models.TextField(_("description"))
    price=models.BigIntegerField(_("price"))
    is_discount=models.BooleanField(_("has_discount"))
    price_with_discount=models.BigIntegerField(_("price_with_discount"))
    category=models.ManyToManyField(Category, verbose_name=_("category"),related_name='product')
    image=models.ImageField(_("image"), upload_to='product_image')
    is_exist=models.BooleanField(_("product_status"))
    created=models.DateTimeField(_("created"), auto_now_add=True)
    updated=models.DateTimeField(_("updated"), auto_now=True)
    properties=models.TextField(_("product_properties"),blank=True,null=True)
    # comments=
    

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def __str__(self):
        return self.title

    def image_tag(self):
        return format_html('<img width=100px height=100px src="{}" />'. format(self.image.url))
