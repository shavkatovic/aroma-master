from django.shortcuts import render


# Create your views here.

def home_view(request):
    return render(request, 'index.html')


def tracking_view(request):
    return render(request, 'tracking-order.html')


def blog_view(request):
    return render(request, 'blog.html')


def cart_view(request):
    return render(request, 'cart.html')


def category_view(request):
    return render(request, 'category.html')


def checkout_view(request):
    return render(request, 'checkout.html')


def confirm_view(request):
    return render(request, 'confirmation.html')


def contact_view(request):
    return render(request, 'contact.html')


def single_blog_view(request):
    return render(request, 'single-blog.html')


def single_product_view(request):
    return render(request, 'single-product.html')
