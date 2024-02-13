from django import forms
from products.models import * 


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'image', 'is_active']


class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['name', 'image', 'is_active']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'brand', 'name', 'description', 'price', 'is_active']


class ImportForm(forms.Form):
    file = forms.FileField(required=False)

    def clean(self):
        cleaned_data = super().clean()
        file = cleaned_data.get('file')
        # if not file:
            # self.add_error("file", "Please import csv file.")
        if not file:
            raise forms.ValidationError("Cannot be left blank!")
        if file.content_type != 'text/csv':
            raise forms.ValidationError("Please import csv file.")

        return cleaned_data
    