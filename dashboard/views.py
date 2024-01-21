from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from dashboard.forms import *


def dashboard(request):
    return render(request, 'admin/dashboard.html')

def category_list(request):
    categories = Categories.objects.all()
    data = {'data': []}
    for category in categories:
        data['data'].append([
            category.id,
            category.name,
        ])
    return JsonResponse(data)

def categories(request):
    return render(request, 'admin/categories.html')

def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.save()
            return redirect('category_list')
    else:
        form = CategoryForm()

    return render(request, 'admin/create_category.html', {'form': form})

def create_brand(request):
    return render(request, 'admin/create_brand.html')
    
def create_product(request):
    return render(request, 'admin/create_product.html')



