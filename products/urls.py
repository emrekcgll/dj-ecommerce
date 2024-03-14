from django.urls import path
from .views import *

urlpatterns = [
    path('search_product_by_category_or_brand/<slug:category_slug>/', search_product_by_category_or_brand, name='search_product_by_category_or_brand'),
    path('search/search_product_by_category_or_brand/<slug:brand_slug>/', search_product_by_category_or_brand, name='search_product_by_category_or_brand'),


    path('categories/', categories, name='h_categories'),
    path('brands/', brands, name='h_brands'),

    path('category/<slug:category_slug>/', products, name='h_products'),
    path('brand/<slug:brand_slug>/', products, name='h_products'),

    path('<slug:brand_slug>/<slug:product_slug>/', product, name='h_product'),


]