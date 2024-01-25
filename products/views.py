from django.shortcuts import render, redirect, get_object_or_404
from products.models import *

def products(request, category_slug=None):
    products = Product.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'home/products.html', {'products': products})


def product(request, brand_slug, product_slug):
    product = get_object_or_404(Product, brand__slug=brand_slug, slug=product_slug)
    return render(request, 'home/product.html', {'product': product})

