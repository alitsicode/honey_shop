from django.db import models
from django.views import generic
from accounts.models import Customeuser
from django.utils.translation import gettext_lazy as _
from django.utils.html import format_html
from django.contrib.contenttypes.fields import GenericRelation
from ckeditor.fields import RichTextField

from comment.models import Comment
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
    description=RichTextField(_("description"))
    price=models.BigIntegerField(_("price"))
    is_discount=models.BooleanField(_("has_discount"),default=False)
    price_with_discount=models.BigIntegerField(_("price_with_discount"),blank=True,null=True)
    category=models.ManyToManyField(Category, verbose_name=_("category"),related_name='product')
    image=models.ImageField(_("image"), upload_to='product_image')
    is_exist=models.BooleanField(_("product_status"),default=True)
    created=models.DateTimeField(_("created"), auto_now_add=True)
    updated=models.DateTimeField(_("updated"), auto_now=True)
    properties=RichTextField(_("product_properties"),blank=True,null=True)
    comments=GenericRelation(Comment)
    

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def __str__(self):
        return self.title

    def image_tag(self):
        return format_html('<img width=100px height=100px src="{}" />'. format(self.image.url))

class Our_Property(models.Model):
    title=models.CharField(_("title"), max_length=100)
    description=models.TextField(_("description"))
    image=models.ImageField(_("image"), upload_to='our_property')
    created=models.DateTimeField(_("created"), auto_now_add=True)
    updated=models.DateTimeField(_("updated"), auto_now=True)

    class Meta:
        verbose_name = _("Our_Property")
        verbose_name_plural = _("Our_Properties")

    def __str__(self):
        return self.title

    def image_tag(self):
        return format_html('<img width=100px height=100px src="{}" />'. format(self.image.url))




class HomeHeader(models.Model):
    title=models.CharField(_("title"), max_length=100)
    short_description=models.TextField(_("short_description"))
    why_our_honey=models.TextField(_("why_our_honey"))
    created=models.DateTimeField(_("created"), auto_now_add=True)
    updated=models.DateTimeField(_("updated"), auto_now=True)


    class Meta:
        verbose_name = _("HomeHeader")
        verbose_name_plural = _("HomeHeaders")

    def __str__(self):
        return self.title


class Like(models.Model):
    user=models.ForeignKey(Customeuser, verbose_name=_("user"), on_delete=models.CASCADE,related_name='like')
    product=models.ForeignKey(Product, verbose_name=_("product"), on_delete=models.CASCADE,related_name='like')
    created=models.DateTimeField(_("created"), auto_now_add=True)
    updated=models.DateTimeField(_("updated"), auto_now=True)
    
    class Meta:
        verbose_name = _("Like")
        verbose_name_plural = _("Likes")

    def __str__(self):
        return self.user.username


class BookMark(models.Model):
    user=models.ForeignKey(Customeuser, verbose_name=_("user"), on_delete=models.CASCADE,related_name='bookmark')
    product=models.ForeignKey(Product, verbose_name=_("product"), on_delete=models.CASCADE,related_name='bookmark')
    created=models.DateTimeField(_("created"), auto_now_add=True)
    updated=models.DateTimeField(_("updated"), auto_now=True)
    
    class Meta:
        verbose_name = _("BookMark")
        verbose_name_plural = _("BookMarks")

    def __str__(self):
        return self.user.username

class Gallery(models.Model):
    title=models.CharField(_("title"), max_length=200,blank=True,null=True)
    image=models.ImageField(_("image"), upload_to='gallery')
    created=models.DateTimeField(_("created"), auto_now_add=True)
    updated=models.DateTimeField(_("updated"), auto_now=True)

    class Meta:
        verbose_name = _("Gallery")
        verbose_name_plural = _("Galleries")

    def image_tag(self):
        return format_html('<img width=100px height=100px src="{}" />'. format(self.image.url))

    
