
from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView
from .models import Customer 
import json

# Create your views here.

def dashboard(request):
    context={"breadcrumb":{"child":"home","parent":"Dashboard"}}
    return render(request, 'dashboard/dashboard.html', context)

def customers(request):
    return render(request, 'dashboard/customers.html')

def create_customer(request):
    return render(request, 'dashboard/create_customer.html')

def returns(request):
    return render(request, 'dashboard/returns.html')

def create_return(request):
    return render(request, 'dashboard/create_return.html')


