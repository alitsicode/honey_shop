from django.db import models
from accounts.models import Customeuser
from django.utils.translation import gettext_lazy as _

# Create your models here.


# ================================================
# not migrations and migrate yet
# ================================================
class Information(models.Model):
    sitename=models.CharField(_("name"), max_length=50)
    logo=models.ImageField(_("Logo"), upload_to='site_logo')
    description=models.TextField(_("description"))
    admins=models.ManyToManyField(Customeuser, verbose_name=_("admin"),blank=True)
    address=models.CharField(_("address"), max_length=50,blank=True,null=True)
    email=models.EmailField(_("email"), max_length=254,blank=True,null=True)
    phone=models.CharField(_("phone"), max_length=11,blank=True,null=True)
    telegram=models.CharField(_("telegram"), max_length=100,blank=True,null=True)
    instagram=models.CharField(_("instagram"), max_length=100,blank=True,null=True)
    class Meta:
        verbose_name = _("Information")
        verbose_name_plural = _("Informations")

    def __str__(self):
        return self.sitename
