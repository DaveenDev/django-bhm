from django.http import HttpResponseBadRequest, JsonResponse, HttpResponseNotAllowed,HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from inventory.models import Category
from .models import Order, Customer, OrderDBView
from .forms import CustomerForm, OrderForm
from main import functions
import json
import pdb; #to remove
# Create your views here.

def orders(request):
    context={"breadcrumb":{"child":"","parent":"Orders"}}
    return render(request, 'order/orders.html', context)

def create_order(request):        
    category_list = functions.get_categories()
    
    context_data = {    
        'categories': category_list,
        "breadcrumb":{"child":"Create order","parent":"New Order"}
    }
    return render(request, 'order/create_order.html', context=context_data)


def create_order_cart(request):  
    context = {"breadcrumb":{"child":"Cart","parent":"New Order"}}
    return render(request, 'order/create_order_cart.html', context)


def create_order_checkout(request):
    
    breadcrumb_context = {"child":"Checkout","parent":"New Order"}
    template_name = 'order/create_order_checkout.html'
    

    if request.method == "GET":
        customer_form = CustomerForm(prefix="customer_form")
        order_form = OrderForm(prefix="order_form")
    
    elif request.method == "POST":
        cart_items = json.loads(request.COOKIES['cart'])
        context = {}
        cust_id = request.POST.get('customer_id')
        
        customer_form = CustomerForm(request.POST, prefix="customer_form")
        order_form = OrderForm(request.POST, prefix = "order_form")
        new_order_no = functions.get_latest_orderno() 
        #pdb.set_trace()
        if not cust_id or cust_id == '':
            # add new customer
            if not customer_form.is_valid():
                context['customer_form'] = customer_form

            if not order_form.is_valid():            
                context['order_form'] = order_form

            if customer_form.is_valid() and order_form.is_valid():                
                # save order data
                customer = customer_form.save()
                order = order_form.save(commit=False)
                
                order.order_no = new_order_no
                order.customer = customer
                order.save()
                messages.success(request, ('Your order was successfully created')) 
                return redirect("order:checkout-thank-you")   
        else:
             
            if order_form.is_valid():
                # get existing customer
                customer = Customer.objects.get(id=cust_id)
                
                order = order_form.save(commit=False)
                order.order_no = new_order_no
                order.customer = customer
                order.save()
                messages.success(request, ('Your order was successfully created')) 
                return redirect("order:checkout-thank-you")   

 
    context = {
            'customer_form': customer_form,
            'order_form': order_form,
            'breadcrumb': breadcrumb_context
    }
    return render(request, template_name ,context)


def order_thankyou(request):
    return render(request, 'order/thank_you.html')

"""@csrf_exempt
def update_cart_session(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    
    if not is_ajax or not request.method == "POST":
        return HttpResponseNotAllowed(['POST'])
    
    request.session['cart'] = request.POST.get('cart')
    return HttpResponse('ok')"""