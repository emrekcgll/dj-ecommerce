from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from dashboard.forms import *
from django.core.paginator import Paginator


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
        ])
    return JsonResponse(data)

def categories(request):
    return render(request, 'dashboard/categories.html')

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
        ])
    return JsonResponse(data)

def brands(request):
    return render(request, 'dashboard/brands.html')

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
    pass

def products(request):
    pass

def create_product(request):
    pass

def update_product(request):
    pass

def delete_product(request):
    pass
