from django.shortcuts import render
from django.http import JsonResponse
from main import functions
from django.views.decorators.csrf import csrf_exempt
from inventory.models import Product
from api.serializers import ProductSerializer
import json
import requests

def inventory(request):
    category_list = functions.get_categories()
    unit_list = functions.get_units()
    product = Product.objects.all()
    products_count = product.count()
    products_list = list(product.values_list('id','sku','name','unit','retail_price','purchased_price','category')[:3])    
    products_list = json.dumps(products_list)
    print(products_list)

    context = {
        "products": products_list,
        "data" : {
            "products": products_list,
            "draw": 50,
            "recordsTotal": products_count,
            "recordsFiltered": products_count
        },
        "units" : unit_list,    
        "categories": category_list,
        "breadcrumb": {
            "child":"Inventory",
            "parent":"Products"
        }
    }

    return render(request, 'inventory/inventory.html', context)


def categories(request):
    context={"breadcrumb":{"child":"Categories","parent":"Products"}}
    return render(request, 'inventory/categories.html', context)


def locations(request):
    context={"breadcrumb":{"child":"Locations","parent":"Products"}}
    return render(request, 'inventory/locations.html', context)


def suppliers(request):
    context={"breadcrumb":{"child":"Suppliers","parent":"Products"}}
    return render(request, 'inventory/suppliers.html', context)

@csrf_exempt
def ajax_products(request):
    if request.method == "GET":
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
    
    return JsonResponse(serializer.data, safe=False)
