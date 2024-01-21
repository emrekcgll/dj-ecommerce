from django.urls import path
from .views import *

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('category-list/', category_list),
    path('categories/', categories, name='categories'),
    path('new-category/', create_category, name='create_category'),
    path('new-brand/', create_brand, name='create_brand'),
    path('new-product/', create_product, name='create_product'),
]