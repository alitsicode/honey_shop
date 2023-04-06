from django.contrib import admin
from .models import Category,Product
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['title','image_tag']
    ordering=['-created']
    list_filter=['title']
    search_fields=['title']
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=['title','price','is_discount','price_with_discount','is_exist','image_tag']
    ordering=['-created','price','is_exist']
    list_filter=['is_exist','category','created']
    search_fields=['title','description']


