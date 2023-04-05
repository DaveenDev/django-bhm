from django import forms
from django.db import models
from django.forms import ModelForm
from main.models import Customer
from .models import Order
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout
from main import functions

PROVINCES = functions.get_provinces()
CITIES = functions.get_regionx12_cities()

class CustomerForm(forms.ModelForm):
    province = forms.ChoiceField(choices=PROVINCES, widget=forms.Select(), required=True)
    city =  forms.ChoiceField(choices=CITIES, widget=forms.Select(), required=True)

    class Meta:
        model = Customer
        exclude = ['created_on', 'updated_on','salesman']
        labels = {
            "customer_name": "Business Name / Customer",
            "contact_no": "Contact Number (mobile/phone)",
            "address1": "Address (house no./block no./street)",
            "address2": "Address (subdivision/barangay)",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit', css_class="btn btn-primary"))
        self.helper.form_method = "POST"    


class OrderForm(forms.ModelForm):
    order_date = forms.DateField(widget=forms.NumberInput(attrs={'type':'date'}))

    class Meta:
        model= Order
        fields = ['order_no','order_date','po_no', 'order_amount']
        labels = {
            'order_no': 'Order No.',
            'order_date': 'Order Date',
            'po_no': 'P.O No.',
            'order_amount': 'Order Amount'
        }
        
    
