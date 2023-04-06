from django.shortcuts import render,get_object_or_404
from django.views import generic
from .models import Product,Category
from django.urls import reverse_lazy
from django.db.models import Q
from .mixins import superusermixin
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def show_home(request):
    last_product=Product.objects.all()[:4]
    return render(request,'pages/home.html',context={'last_product':last_product})

class ProductListView(generic.ListView):
    model = Product
    template_name = "pages/product_list.html"
    context_object_name='products'
    
class Product_By_Category(generic.ListView):
    model=Category
    template_name='pages/product_list.html'
    def get_context_data(self, **kwargs):
        pk=self.kwargs['pk']
        categorie=get_object_or_404(Category,pk=pk)
        product_category=categorie.product.all()
        context = super().get_context_data(**kwargs)
        context["products"] = product_category
        return context

class ProductDetailView(generic.DetailView):
    model = Product
    template_name = "pages/product_detail.html"
    context_object_name='product'

class ProductSearchListView(generic.ListView):
    template_name = "pages/product_list.html"
    model=Product
    def get_context_data(self, **kwargs):
        query=self.request.GET.get("search")
        context = super().get_context_data(**kwargs)
        context["products"] = Product.objects.all().filter(Q(title__icontains=query) | Q(description__icontains=query))  
        return context

class ProductUpdateView(superusermixin,LoginRequiredMixin,generic.UpdateView):
    model = Product
    template_name = "pages/product_update.html"
    fields='__all__'
    context_object_name='product'
    success_url=reverse_lazy('home')

class ProductDeleteView(superusermixin,LoginRequiredMixin,generic.DeleteView):
    model = Product
    template_name = "pages/product_delete.html"
    success_url=reverse_lazy('home')
    context_object_name='product'



    


