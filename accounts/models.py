from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class Customeuser(AbstractUser):
    email=models.EmailField(_('email'),max_length=254,unique=True)
    first_name=models.CharField(_('first_name'),max_length=200)
    last_name=models.CharField(_('last_name'),max_length=200)
    avatar=models.ImageField(_('avatar'),null=True,blank=True,upload_to='user_avatar')
    phone=models.CharField(_('phone'),max_length=11,null=True,blank=True)

    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name=_('CustomeUser') 
