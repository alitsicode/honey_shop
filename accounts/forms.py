from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from . models import Customeuser
from django import forms

class customusercreationform(UserCreationForm):
    class Meta:
        model=Customeuser
        fields=UserCreationForm.Meta.fields + ('avatar','email','phone')

class customuserchangeform(UserChangeForm):
    class Meta:
        model=Customeuser
        fields=UserChangeForm.Meta.fields

class profile_form(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        user=kwargs.pop('user')
        super(profile_form,self).__init__(*args, **kwargs)
        if not user.is_superuser:
            self.fields['date_joined'].disabled=True
    class Meta:
        model= Customeuser
        fields=['username','phone','first_name','last_name','avatar','email','date_joined']