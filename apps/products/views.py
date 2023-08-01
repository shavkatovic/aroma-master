from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, DetailView, ListView

from products.models import Product


# Create your views here.

class Index(ListView):
    queryset = Product.objects.all()
    context_object_name = 'products'
    template_name = 'index.html'


class Tracking_view(TemplateView):
    template_name = 'tracking-order.html'


class Blog_view(TemplateView):
    template_name = 'blog.html'


class Cart_view(TemplateView):
    template_name = 'cart.html'


class Category_view(TemplateView):
    template_name = 'category.html'


class Checkout_view(TemplateView):
    template_name = 'checkout.html'


class Confirm_view(TemplateView):
    template_name = 'confirmation.html'


class Contact_view(TemplateView):
    template_name = 'contact.html'


class Single_blog_view(TemplateView):
    template_name = 'single-blog.html'


class Single_product_view(DetailView):
    queryset = Product.objects.all()
    context_object_name = 'product'
    template_name = 'single-product.html'
