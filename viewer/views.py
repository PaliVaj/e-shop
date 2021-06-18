from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import ListView, DetailView, TemplateView, CreateView, DeleteView, UpdateView

from viewer.form import ProductModelForm
from viewer.models import Product, Brand


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

class ProductCreateView(LoginRequiredMixin, CreateView):
    template_name = 'form.html'
    form_class = ProductModelForm
    success_url = reverse_lazy('')

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'form.html'
    Model = Product
    form_class = ProductModelForm
    success_url = reverse_lazy('')

class ProductDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'product_confirm_delete'
    Model = Product
    success_url = reverse_lazy('')

# Brand View



class CarbrandListView(ListView):
    template_name = "brand_list.html"
    context_object_name = "carbrandlist"

    def get_queryset(self):
        content = {
            'carbrand': self.kwargs['brand'],
            'products': Product.objects.filter(brand__name=self.kwargs['brand'])
        }
        return content

# Search function

def search_product(request):
    """ search function  """
    if request.method == "POST":
        query_name = request.POST.get('name', None)
        if query_name:
            results = Product.objects.filter(name__contains=query_name)
            return render(request, 'products.html', {"results":results})

    return render(request, 'products.html')