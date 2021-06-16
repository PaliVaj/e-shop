from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import ListView, DetailView, TemplateView, CreateView

from viewer.form import ProductModelForm
from viewer.models import  Product


class ProductView(ListView):
    template_name = 'products.html'
    model = Product

class ProductDetailView(DetailView):
    model = Product
    template_name = 'productsdetail.html'
    #queryset = Product.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


# Vytvorenie CreateViewForm

class ProductCreateView(CreateView):
    template_name = 'form.html'
    form_class = ProductModelForm
    success_url = reverse_lazy('')

