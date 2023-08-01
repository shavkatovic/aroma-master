from django.contrib import admin
from django.urls import path
from .views import home_view, tracking_view, blog_view, cart_view, category_view, checkout_view, confirm_view, contact_view, single_blog_view, single_product_view

urlpatterns = [
    path('', home_view, name='home'),
    path('tracking/', tracking_view, name='tracking'),
    path('blog/', blog_view, name='blog'),
    path('cart/', cart_view, name='cart'),
    path('category/', category_view, name='category'),
    path('checkout/', checkout_view, name='checkout'),
    path('confirm/', confirm_view, name='confirm'),
    path('contact/', contact_view, name='contact'),
    path('single_blog/', single_blog_view, name='single-blog'),
    path('single_product/', single_product_view, name='single-product'),
]
