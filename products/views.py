from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from products.models import *


def categories(request):
    return render(request, 'home/categories.html')


def brands(request):
    brands = Brand.objects
    selected_char = request.GET.get('char', 'a')
    if selected_char == '0-9':
        filtered_brands = brands.exclude(name__iregex=r'^[A-Z]').order_by('name')
    else:    
        filtered_brands = brands.filter(name__istartswith=selected_char)
    
    paginator = Paginator(filtered_brands, 40)
    page = request.GET.get("page")
    try:
        data = paginator.page(page)
        page_range = paginator.page_range[max(0, data.number - 3): data.number + 2]
    except PageNotAnInteger:
        data = paginator.page(1)
        page_range = paginator.page_range[:5]
    except EmptyPage:
        data = paginator.page(paginator.num_pages)
        page_range = paginator.page_range[-5:]
    total_items = paginator.count
    items_per_page = len(data)

    characters = [chr(i) for i in range(65, 91)] + ['0-9']
    return render(request, 'home/brands.html', {'data': data, 'selected_char': selected_char, 'characters': characters, 
                                                'total_items': total_items, 'items_per_page': items_per_page, 
                                                'page_range': page_range, })


def products(request, category_slug=None, brand_slug=None):
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)
        
        paginator = Paginator(products, 10)
        page = request.GET.get("page")
        try:
            data = paginator.page(page)
            page_range = paginator.page_range[max(0, data.number - 3): data.number + 2]
        except PageNotAnInteger:
            data = paginator.page(1)
            page_range = paginator.page_range[:5]
        except EmptyPage:
            data = paginator.page(paginator.num_pages)
            page_range = paginator.page_range[-5:]

        total_items = paginator.count
        items_per_page = len(data)
        return render(request, 'home/products.html', {'category': category, 'data': data, 
                                                      'total_items': total_items, 
                                                      'items_per_page': items_per_page, 
                                                      'page_range': page_range})

    if brand_slug:
        brand = get_object_or_404(Brand, slug=brand_slug)
        products = Product.objects.filter(brand=brand)
        
        paginator = Paginator(products, 10)
        page = request.GET.get("page")
        try:
            data = paginator.page(page)
            page_range = paginator.page_range[max(0, data.number - 3): data.number + 2]
        except PageNotAnInteger:
            data = paginator.page(1)
            page_range = paginator.page_range[:5]
        except EmptyPage:
            data = paginator.page(paginator.num_pages)
            page_range = paginator.page_range[-5:]

        total_items = paginator.count
        items_per_page = len(data)
        return render(request, 'home/products.html', {'brand': brand, 'data': data, 
                                                      'total_items': total_items, 
                                                      'items_per_page': items_per_page, 
                                                      'page_range': page_range})


def product(request, brand_slug, product_slug):
    product = get_object_or_404(Product, brand__slug=brand_slug, slug=product_slug)
    return render(request, 'home/product.html', {'product': product})