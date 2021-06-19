"""Eshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views
from django.contrib.auth.views import LoginView, LogoutView
from django.template import base
from django.urls import path, re_path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from accounts.views import SubmittableLoginView, SignUpView
from viewer.views import ProductView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView, \
    CarbrandListView, search_product
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', LoginView.as_view(), name='login'),


    path('products', ProductView.as_view(), name='products'),
    path('create', ProductCreateView.as_view(), name='create'),
    path('update/<int:pk>', ProductUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', ProductDeleteView.as_view(), name='delete'),
    path('', ProductView.as_view(), name='index'),
    path('<int:pk>/', ProductDetailView.as_view(), name='products_detail'),
    path('brands/<brand>', CarbrandListView.as_view(), name='brands_products'),
    path('accounts/login', SubmittableLoginView.as_view(), name='login'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
    path('accounts/sign-up/', SignUpView.as_view(), name='sign_up'),
    path('search/', search_product, name='search'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



