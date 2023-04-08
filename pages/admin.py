from django.contrib import admin
from .models import Category,Product,Our_Property,HomeHeader,Like,BookMark,Gallery
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

@admin.register(Our_Property)
class Our_PropertyAdmin(admin.ModelAdmin):
    list_display=['title','image_tag']
    search_fields=['title','description']
    ordering=['-created']
    list_filter=['created']

@admin.register(HomeHeader)
class HomeHeaderAdmin(admin.ModelAdmin):
    list_display=['title']
    ordering=['-created']
    list_filter=['created']
    search_fields=['title']


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_filter=['user','product']
    ordering=['-created']
    list_filter=['product','user','created']
    search_fields=['product','user']


@admin.register(BookMark)
class BookMarkAdmin(admin.ModelAdmin):
    list_filter=['user','product']
    ordering=['-created']
    list_filter=['product','user','created']
    search_fields=['product','user']


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display=['image_tag']
    



