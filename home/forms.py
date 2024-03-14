from django import forms
from home.models import Country
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Field

class RequestForm(forms.Form):
    name_surname = forms.CharField(label='Name Surname', max_length=256)
    company_name = forms.CharField(label='Company Name', required=False, max_length=256)
    email = forms.EmailField(label='Email', max_length=256)
    phone = forms.CharField(label='Phone', required=False, max_length=50)
    country = forms.ModelChoiceField(
        label='Country', 
        queryset=Country.objects.all(),
        to_field_name='mn',
        empty_label='Select country')
    city = forms.CharField(label='City', required=False)
    requested_product = forms.CharField(label='Requested Product', max_length=256)
    message = forms.CharField(label='Message', widget=forms.Textarea(attrs={'rows': 4, 'cols': 40}), help_text='You can give detailed information about the product, how many you want or your special requests.')

    def __init__(self, *args, requested_product=None, **kwargs):
        super(RequestForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(
                Field('name_surname', css_class=''),
                Field('email', css_class=''),
                Field('country', css_class=''),
                css_class='col-md-6'
            ),
            Div(
                Field('company_name', css_class=''),
                Field('phone', css_class=''),
                Field('city', css_class=''),
                css_class='col-md-6'
            ),
            Div(
                Field('requested_product', css_class=''),
                Field('message', css_class=''),
                css_class='col-md-12'
            ),
        )

        if requested_product:
            self.fields['requested_product'].initial = requested_product


class ContactForm(forms.Form):
    name_surname = forms.CharField(label='Full Name', max_length=256)
    email = forms.EmailField(label='Email', max_length=256)
    phone = forms.CharField(label='Phone', max_length=256, required=False)
    message = forms.CharField(label='Message', widget=forms.Textarea(attrs={'rows': 4}))