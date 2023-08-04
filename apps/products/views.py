from django.http.response import HttpResponseNotAllowed
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, DetailView, CreateView
from django.urls import reverse_lazy
from django.shortcuts import redirect, get_object_or_404, reverse
from products.forms import CommentForm, ReplayCommentForm
from products.models import Product, Blog, Comment, ReplayComment


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


class SingleProductView(CreateView, DetailView):
    model = Product
    form_class = CommentForm
    template_name = 'single-product.html'
    context_object_name = 'product'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.all()
        return context


# class ReplayCommentCreateView(CreateView):
#     template_name = 'single-product.html'
#     model = ReplayComment
#     form_class = ReplayCommentForm
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         product_pk = self.kwargs['pk']
#         context['product'] = get_object_or_404(Product, pk=product_pk)
#         context['com'] = Comment.objects.filter(product=context['product'])
#         context['rk'] = self.kwargs['rk']
#         context['replay_comment'] = ReplayComment.objects.all()
#         return context
#
#     def get_success_url(self):
#         return reverse('home')
#
#     def form_valid(self, form):
#         product_pk = self.kwargs['pk']
#         product = get_object_or_404(Product, pk=product_pk)
#         form.instance.product = product
#         return super().form_valid(form)
