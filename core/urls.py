from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('web/', include('dashboard.urls')),
    path('orders/', include('orders.urls')),
    path('', include('home.urls')),
    path('', include('products.urls')),
]
