from django.http.response import HttpResponseNotAllowed
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, DetailView, ListView

from products.models import Product, Blog


# Create your views here.

class Index(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        context['blogs'] = Blog.objects.all()
        return context



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
