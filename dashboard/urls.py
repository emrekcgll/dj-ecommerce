from django.urls import path
from .views import *

urlpatterns = [
    path('', dashboard, name='dashboard'),


    path('category-list/', category_list),
    path('product-list-by-category/<int:pk>/', product_list_by_category),
    path('categories/', categories, name='categories'),
    path('category/<int:pk>/', category, name='category'),
    path('new-category/', create_category, name='create_category'),
    path('update-category/<int:pk>/', update_category, name='update_cateogory'),
    path('delete-category/<int:pk>/', delete_category),


    path('brand-list/', brand_list),
    path('product-list-by-brand/<int:pk>/', product_list_by_brand),
    path('brands/', brands, name='brands'),
    path('brand/<int:pk>/', brand, name='brand'),
    path('new-brand/', create_brand, name='create_brand'),
    path('update-brand/<int:pk>/', update_brand, name='update_brand'),
    path('delete-brand/<int:pk>/', delete_brand),


    path('product-list/', product_list),
    path('products/', products, name='products'),
    path('new-product/', create_product, name='create_product'),
    path('update-product/<int:pk>/', update_product, name='update_product'),
    path('delete-product/<int:pk>/', delete_product),


    path('import-data/', import_data, name='import-data'),
]