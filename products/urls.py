from django.urls import path
from .views import *

urlpatterns = [
    path('categories/', categories, name='h_categories'),
    path('brands/', brands, name='h_brands'),

    path('category/<slug:category_slug>/', products, name='h_products'),
    path('brand/<slug:brand_slug>/', products, name='h_products'),

    path('<slug:brand_slug>/<slug:product_slug>/', product, name='h_product'),
]