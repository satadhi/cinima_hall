from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404

from .models import Product
# Create your views here.

class ProductListView(ListView):
    queryset = Product.objects.all()
 # not fully implemented !

def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'qs': queryset
    }
    return render(request, "products/list.html",context)

def product_detail_view(request,pk=None , *args, **kwargs):
    #instance = Product.objects.get(pk=pk)
    instance = get_object_or_404(Product,pk=pk)#id
    print(instance)
    context = {
        'object': instance
    }
    return render(request, "products/detail.html",context)
