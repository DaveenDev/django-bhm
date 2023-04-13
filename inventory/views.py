from django.shortcuts import render
from django.http import JsonResponse
from main import functions
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView
from inventory.models import Product
from api.serializers import ProductSerializer
from .forms import ProductForm

def inventory(request):
    category_list = functions.get_categories()
    unit_list = functions.get_units()
    location_list = functions.get_locations()    
    context = {        
        "units" : unit_list,    
        "categories": category_list,
        "locations": location_list,
        "breadcrumb": {
            "child":"Inventory",
            "parent":"Products"
        }
    }

    return render(request, 'inventory/inventory.html', context)

class NewProductView(CreateView):
    model = Product
    form_class = ProductForm
    template_name="inventory/new-product.html"
    success_url = "new-product/success"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['breadcrumb']= {"child":"Add Product","parent":"Product"}
        return context
    
def success_view(request):
    return render(request, 'inventory/success.html')


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
