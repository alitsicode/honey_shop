from django.urls import path
from . import views
urlpatterns = [
    path('',views.show_home,name='home'),
    path('products/',views.ProductListView.as_view(),name='products'),
    path('product_detail/<int:pk>',views.ProductDetailView.as_view(),name='product_detail'),
    path('product_category/<int:pk>',views.Product_By_Category.as_view(),name='product_category'),
    path('search/',views.ProductSearchListView.as_view(),name='search'),
]