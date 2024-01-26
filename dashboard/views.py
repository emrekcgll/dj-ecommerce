import os
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from dashboard.forms import *
from django.core.paginator import Paginator
from django.conf import settings


def dashboard(request):
    return render(request, 'dashboard/dashboard.html')


def category_list(request):
    # Fetch all categories
    categories = Category.objects.all()
    # Get parameters from DataTables AJAX request
    start = int(request.GET.get('start', 0))
    length = int(request.GET.get('length', 10))
    min_length = 10
    max_length = 100
    length = max(min_length, min(length, max_length))
    # Get search parameter
    search_value = request.GET.get('search[value]', '')
    # Apply search filter if search value is provided
    if 30 > len(search_value) > 3:
        categories = categories.filter(name__icontains=search_value)
    # Paginate the queryset
    paginator = Paginator(categories, length)
    categories_on_page = paginator.page((start // length) + 1)
    # Prepare data for JSON response
    data = {
        'data': [],
        'recordsTotal': categories.count(),
        'recordsFiltered': paginator.count,
    }
    # Populate data with the paginated categories
    for category in categories_on_page:
        data['data'].append([
            category.id,
            category.name,
            category.product_count()
        ])
    return JsonResponse(data)


def categories(request):
    return render(request, 'dashboard/categories.html')


def category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    return render(request, 'dashboard/category.html', {'category': category})


def product_list_by_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    products = Product.objects.filter(category=category)
    start = int(request.GET.get('start', 0))
    length = int(request.GET.get('length', 10))
    min_length = 10
    max_length = 100
    length = max(min_length, min(length, max_length))
    search_value = request.GET.get('search[value]', '')
    if 30 > len(search_value) > 3:
        products = products.filter(name__icontains=search_value)
    paginator = Paginator(products, length)
    products_on_page = paginator.page((start // length) + 1)
    data = {
        'data': [],
        'recordsTotal': products.count(),
        'recordsFiltered': paginator.count,
    }
    for product in products_on_page:
        data['data'].append([
            product.id,
            product.name,
        ])
    return JsonResponse(data)


def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.created_by = request.user
            category.save()
            return redirect('categories')
    else:
        form = CategoryForm()
    return render(request, 'dashboard/create_category.html', {'form': form})


def update_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            category = form.save(commit=False)
            category.save()
            return redirect('categories')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'dashboard/update_category.html', {'form': form})


def delete_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return JsonResponse({'message': 'Category deleted successfully.'})
    return JsonResponse({'message': 'Category delete operation is unsuccessful.'}, status=400)


def brand_list(request):
    brands = Brand.objects.all()
    start = int(request.GET.get('start', 0))
    length = int(request.GET.get('length', 10))
    min_length = 10
    max_length = 100
    length = max(min_length, min(length, max_length))
    search_value = request.GET.get('search[value]', '')
    if 30 > len(search_value) > 3:
        brands = brands.filter(name__icontains=search_value)
    paginator = Paginator(brands, length)
    brands_on_page = paginator.page((start // length) + 1)
    data = {
        'data': [],
        'recordsTotal': brands.count(),
        'recordsFiltered': paginator.count,
    }
    for brand in brands_on_page:
        data['data'].append([
            brand.id,
            brand.name,
            brand.product_count()
        ])
    return JsonResponse(data)


def brands(request):
    return render(request, 'dashboard/brands.html')


def brand(request, pk):
    brand = get_object_or_404(Brand, pk=pk)
    return render(request, 'dashboard/brand.html')


def product_list_by_brand(request, pk):
    brand = get_object_or_404(Brand, pk=pk)
    products = Product.objects.filter(brand=brand)
    start = int(request.GET.get('start', 0))
    length = int(request.GET.get('length', 10))
    min_length = 10
    max_length = 100
    length = max(min_length, min(length, max_length))
    search_value = request.GET.get('search[value]', '')
    if 30 > len(search_value) > 3:
        products = products.filter(name__icontains=search_value)
    paginator = Paginator(products, length)
    products_on_page = paginator.page((start // length) + 1)
    data = {
        'data': [],
        'recordsTotal': products.count(),
        'recordsFiltered': paginator.count,
    }
    for product in products_on_page:
        data['data'].append([
            product.id,
            product.name,
        ])
    return JsonResponse(data)


def create_brand(request):
    if request.method == 'POST':
        form = BrandForm(request.POST)
        if form.is_valid():
            brand = form.save(commit=False)
            brand.created_by = request.user
            brand.save()
            return redirect('brands')
    else:
        form = CategoryForm()
    return render(request, 'dashboard/create_brand.html', {'form': form})


def update_brand(request, pk):
    brand = get_object_or_404(Brand, pk=pk)
    if request.method == 'POST':
        form = BrandForm(request.POST, instance=brand)
        if form.is_valid():
            brand = form.save(commit=False)
            brand.save()
            return redirect('brands')
    else:
        form = BrandForm(instance=brand)
    return render(request, 'dashboard/update_brand.html', {'form': form})


def delete_brand(request, pk):
    brand = get_object_or_404(Brand, pk=pk)
    if request.method == 'POST':
        brand.delete()
        return JsonResponse({'message': 'Brand deleted successfully.'})
    return JsonResponse({'message': 'Brand delete operation is unsuccessful.'}, status=400)


def product_list(request):
    products = Product.objects.all()
    start = int(request.GET.get('start', 0))
    length = int(request.GET.get('length', 10))
    min_length = 10
    max_length = 100
    length = max(min_length, min(length, max_length))
    search_value = request.GET.get('search[value]', '')
    if 30 > len(search_value) > 3:
        products = products.filter(name__icontains=search_value)
    paginator = Paginator(products, length)
    products_on_page = paginator.page((start // length) + 1)
    data = {
        'data': [],
        'recordsTotal': products.count(),
        'recordsFiltered': paginator.count,
    }
    for product in products_on_page:
        data['data'].append([
            product.id,
            product.first_image(),
            product.category.name,
            product.brand.name,
            product.name,
        ])
        print(data)
    return JsonResponse(data)


def products(request):
    return render(request, 'dashboard/products.html')


def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.created_by = request.user
            product.save()
            product_instance = get_object_or_404(Product, pk=product.pk)
            images = request.FILES.getlist("images")
            for image in images:
                Image.objects.create(product=product_instance, image=image)
            return redirect('products')
    else:
        form = ProductForm()
    return render(request, 'dashboard/create_product.html', {'form': form})


def update_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product_images = get_list_or_404(Image, product=product)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            product = form.save(commit=False)
            product.save()
            return redirect('products')
    else:
        form = ProductForm(instance=product)
    return render(request, 'dashboard/update_product.html', {'form': form, 'product_images': product_images})


def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        for img in Image.objects.filter(product=product):
            os.remove(os.path.join(settings.MEDIA_ROOT, img.image.name))
            img.delete()
        product.delete()
        return JsonResponse({'message': 'Product deleted successfully.'})
    return JsonResponse({'message': 'Product delete operation is unsuccessful.'}, status=400)
