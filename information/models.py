from django.db import models
from accounts.models import Customeuser
from django.utils.translation import gettext_lazy as _
from django.utils.html import format_html

# Create your models here.


# ================================================
# not migrations and migrate yet
# ================================================
class AboutUs(models.Model):
    sitename=models.CharField(_("name"), max_length=50)
    logo=models.ImageField(_("Logo"), upload_to='site_logo')
    image=models.ImageField(_("image"), upload_to='about_image')
    description=models.TextField(_("description"))
    admins=models.ManyToManyField(Customeuser, verbose_name=_("admin"),blank=True)
    address=models.CharField(_("address"), max_length=50,blank=True,null=True)
    email=models.EmailField(_("email"), max_length=254,blank=True,null=True)
    phone=models.CharField(_("phone"), max_length=11,blank=True,null=True)
    telegram=models.CharField(_("telegram"), max_length=100,blank=True,null=True)
    instagram=models.CharField(_("instagram"), max_length=100,blank=True,null=True)
    date_create=models.DateTimeField(_("date_create"), auto_now_add=True)
    date_modified=models.DateTimeField(_("date_modified"), auto_now=True)
    class Meta:
        verbose_name = _("AboutUs")
        verbose_name_plural = _("AboutUs")

    def __str__(self):
        return self.sitename
    def logo_tag(self):
        return format_html('<img width=100px height=100px src="{}" />'. format(self.logo.url))

class ContactUs(models.Model):
    user=models.ForeignKey(Customeuser, verbose_name=_("user"), on_delete=models.CASCADE)
    text=models.TextField(_("text"))
    date_create=models.DateTimeField(_("date_create"), auto_now_add=True)
    date_modified=models.DateTimeField(_("date_modified"), auto_now=True)
    
    class Meta:
        verbose_name = _("ContactUs")
        verbose_name_plural = _("ContactUs")

    def __str__(self):
        return self.user
