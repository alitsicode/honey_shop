from django.shortcuts import render,get_object_or_404,redirect
from django.views import generic
from .models import Product,Category,HomeHeader,Our_Property,Like,BookMark,Gallery
from django.urls import reverse_lazy
from django.db.models import Q
from django.http import JsonResponse
from .mixins import superusermixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


# Create your views here.

def show_home(request):
    last_product=Product.objects.all()[:4]
    home_header=HomeHeader.objects.last()
    galleries=Gallery.objects.all()[:4]
    our_property=Our_Property.objects.all()[:4]
    return render(request,'pages/home.html',context={'last_product':last_product,'home_header':home_header,'our_property':our_property,'galleries':galleries,})

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

class ProductDetailView(LoginRequiredMixin,generic.DetailView):
    model = Product
    template_name = "pages/product_detail.html"
    def get_context_data(self, **kwargs):
        pk = self.kwargs['pk']
        product=get_object_or_404(Product,pk=pk)
        context = super().get_context_data(**kwargs)
        context['product'] = product
        if self.request.user.bookmark.filter(product=product,user=self.request.user).exists(): #related_name from user to find like or not
            context["saved"] = True
        else:
            context["saved"] = False
        if self.request.user.like.filter(product=product,user=self.request.user).exists(): #related_name from user to find like or not
            context["liked"] = True
        else:
            context["liked"] = False
        return context

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

@login_required
def bookmark(request,pk):
    product=get_object_or_404(Product,pk=pk)
    try:
        save=BookMark.objects.get(product=product,user=request.user)
        save.delete()
    except:
        BookMark.objects.create(product=product,user=request.user)
        return JsonResponse({"response":"saved"})
    return redirect('product_detail',pk)

@login_required
def like(request,pk):
    product=get_object_or_404(Product,pk=pk)
    try:
        like=Like.objects.get(product=product,user=request.user)
        like.delete()
    except:
        Like.objects.create(product=product,user=request.user)
        return JsonResponse({"response":"liked"})
    return redirect('product_detail',pk)



    


