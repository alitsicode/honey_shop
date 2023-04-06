from django.contrib import admin
from .models import AboutUs,ContactUs
# Register your models here.

@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display=['sitename','address','logo_tag','email','phone','telegram','instagram']
    ordering=['-date_create']

@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display=['user']
    ordering=['-date_create']
    search_fields=['user']

