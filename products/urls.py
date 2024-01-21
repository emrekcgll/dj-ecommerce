from django.urls import path
from .views import *

urlpatterns = [
    path('shop/', products, name='products'),
    path('shop/<slug:category_slug>/', products, name='products'),

    path('shop/<slug:brand_slug>/<slug:product_slug>/', product, name='product')
]