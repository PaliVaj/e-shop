from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

from viewer.models import  Product


class ProductView(ListView):
    template_name = 'products.html'
    model = Product

class ProductDetailView(DetailView):
    model = Product
    template_name = 'productsdetail.html'
    #queryset = Product.objects.all()