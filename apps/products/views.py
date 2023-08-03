from django.views.generic import TemplateView, DetailView, ListView
from httpx import post
from products.models import Product, Blog
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.contrib.auth.models import User


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

    def post(self, request, *args, **kwargs):
        data = super().get(request, *args, **kwargs)
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        message = request.POST.get('message', '')
        m = f'''📥 New mail\n📩 From: {email}\n👱 Name: {name}\n📄 Message: {message}'''
        send_message(5654406350, m)
        return data


class Single_blog_view(TemplateView):
    template_name = 'single-blog.html'


class Single_product_view(DetailView):
    queryset = Product.objects.all()
    context_object_name = 'product'
    template_name = 'single-product.html'


def send_message(chat_id, message):
    url = f'https://api.telegram.org/bot6133066485:AAH2TIFdMuj2LRlfZOV1TUFqOwKKYF37oeo/sendMessage'
    params = {
        'chat_id': chat_id,
        'text': message
    }
    post(url, params=params)
