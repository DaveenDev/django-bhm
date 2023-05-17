from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import JsonResponse, HttpResponseRedirect
from main import functions
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView, UpdateView
from inventory.models import Product, Inventory
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
    success_url = "success"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)        
        context['breadcrumb']= {"child":"Add Product","parent":"Product"}
        return context
    
    def form_valid(self, form):
        self.object = form.save()        
        default_loc = functions.get_default_location_id()
        product_inv  = Inventory(product = self.object, stock_level=0, location_id=default_loc)
        product_inv.save()
        
        #print(functions.debug_esc('31;1;4') + 'Form Data')
        #print(form.cleaned_data)
        #print(functions.debug_esc(0))
        return HttpResponseRedirect(self.get_success_url)
    
class ProductDetail(UpdateView):
    model = Product
    form_class = ProductForm
    template_name="inventory/product-detail.html"
    success_url = "/products/success"
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['breadcrumb']= {"child":"Product detail","parent":"Product"}
        return context
    
    """def form_valid(self, form, **kwargs):
        form.save()        
        return HttpResponseRedirect(self.success_url)    """
    
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
