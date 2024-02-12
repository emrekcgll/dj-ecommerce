from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='h_home'),
    path('about/', about, name='h_about'),
    path('contact/', contact, name='h_contact'),
    path('faq/', faq, name='h_faq'),
    path('get-request/', get_request, name='h_get_request'),
]
