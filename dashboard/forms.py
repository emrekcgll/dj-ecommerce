from django import forms
from products.models import * 


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Categories
        fields = ['name']

