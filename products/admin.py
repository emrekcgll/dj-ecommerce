from django.contrib import admin
from products.models import *

admin.site.register(Categories)
admin.site.register(Brands)
admin.site.register(Products)
admin.site.register(Images)