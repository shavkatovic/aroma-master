from django.contrib import admin
from django.urls import path
from .views import Index, Tracking_view, Blog_view, Cart_view, Category_view, Checkout_view, Confirm_view, Contact_view, \
    Single_blog_view, SingleProductView

urlpatterns = [
    path('', Index.as_view(), name='home'),
    path('tracking/', Tracking_view.as_view(), name='tracking'),
    path('blog/', Blog_view.as_view(), name='blog'),
    path('cart/', Cart_view.as_view(), name='cart'),
    path('category/', Category_view.as_view(), name='category'),
    path('checkout/', Checkout_view.as_view(), name='checkout'),
    path('confirm/', Confirm_view.as_view(), name='confirm'),
    path('contact/', Contact_view.as_view(), name='contact'),
    path('single/<int:pk>/', Single_blog_view.as_view(), name='single-blog'),
    path('product/<int:pk>', SingleProductView.as_view(), name='single-product'),
    # path('replay/<int:pk>/<int:rk>', ReplayCommentCreateView.as_view(), name='replay-comment')
]
