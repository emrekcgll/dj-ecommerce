from django.db import models

class Country(models.Model):
    name = models.TextField(unique=True)
    mn = models.TextField(unique=True)
    is_active = models.BooleanField(default=True)