from django.urls import path
from .views import *

urlpatterns = [
    path('', h_login, name='h_login'),
    path('logout/', h_logout, name='h_logout'),
]
