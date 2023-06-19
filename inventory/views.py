from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse, HttpResponseNotFound, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView, UpdateView
from django.db import IntegrityError
from inventory.models import Product, InvLocation, Category, Supplier
from api.serializers import ProductSerializer
from .forms import ProductForm
from main import functions
import json
import requests

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
        context['breadcrumb']= {"child":"Add Product","parent":"Product"}
        return context
    
    def form_valid(self, form):
        self.object = form.save()
        print(functions.debug_esc('31;1;4') + 'Form Data')
        print(form.cleaned_data)
        print(functions.debug_esc(0))
        return HttpResponseRedirect(self.get_success_url)
    
class ProductDetail(UpdateView):
    model = Product
    form_class = ProductForm
    template_name="inventory/product-detail.html"
    success_url = "new-product/success"
    fields = "__all__"

    def get_queryset(self, **kwargs):
        id = int(kwargs.pk)
        product = Product.objects.get(pk=id)
        return product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['breadcrumb']= {"child":"Product detail","parent":"Product"}
        return context

    
def success_view(request):
    return render(request, 'inventory/success.html')


def categories(request):
    categories = list(Category.objects.all().values('id', 'name'))  
    category_list = json.dumps(categories)
    context={
        "breadcrumb": {
                "child":"Categories",
                "parent":"Products"
        },
        "category_list": category_list
    }
    return render(request, 'inventory/categories.html', context)
# CATEGORY ADD
def category_add(request):    
    cat_name = request.POST.get('category_name')
    cat_name = cat_name.capitalize()    
    try:
        Category.objects.create(name=cat_name)
        return HttpResponse("New category was added")
    except IntegrityError as e:
        return HttpResponseBadRequest("Category name already existed")
    
# CATEGORY UPDATE
def category_update(request):
    cat_id = request.POST.get('category_id')
    cat_name = request.POST.get('category_name')
    category = get_object_or_404(Category, id=cat_id)
    if category is not None:
        try:
            category.name = cat_name.capitalize()
            category.save()
            return HttpResponse("Category name was updated")
        except IntegrityError as e:
            return HttpResponseBadRequest("Category name already existed.")
    else:
        return HttpResponseBadRequest("Unable to update a category that does not exist in the database.")
# CATEGORY DELETE
def category_delete(request):
    cat_id = request.POST.get('category_id')
    category = get_object_or_404(Category, id=cat_id)
    if category is not None:
        category.delete()
        return HttpResponse("Category was deleted")
    else:
        return HttpResponseBadRequest("Unable to delete a category that does not exist in the database.")


def locations(request):
    locations = list(InvLocation.objects.all().values())
    locations_list = json.dumps(locations)
    
    context={
        "breadcrumb": {
                "child":"Locations",
                "parent":"Products"
        },
        "locations_list": locations_list
    }
    return render(request, 'inventory/locations.html', context)

def location_add(request):   
    
    loc_name = request.POST['location_name']
    loc_name = loc_name.capitalize()    
    address = request.POST['address']
    city = request.POST['city']
    region = request.POST['region']
    post_code = request.POST['post_code']
    country = request.POST['country']
    try:
        InvLocation.objects.create(name=loc_name,
                                address=address,
                                city=city,
                                region=region,
                                post_code=post_code,
                                country=country)
        return HttpResponse("New location was added")
    except IntegrityError as e:
        return HttpResponseBadRequest("Location name already existed")

def location_update(request):    
    loc_id = request.POST.get('location_id')
    loc_name = request.POST.get('location_name')
    location = get_object_or_404(InvLocation, id=loc_id)
    if location is not None:
        try:
            location.name = loc_name.capitalize()
            location.address = request.POST['address']
            location.city = request.POST['city']
            location.region =  request.POST['region']
            location.post_code = request.POST['post_code']
            location.country =  request.POST['country']
            location.save()
            return HttpResponse("Location name was updated")
        except IntegrityError as e:
            return HttpResponseBadRequest("Location name already existed.")
    else:
        return HttpResponseBadRequest("Unable to update a location that does not exist in the database.")

def location_delete(request):
    loc_id = request.POST.get('location_id')
    location = get_object_or_404(InvLocation, id=loc_id)
    if location is not None:
        location.delete()
        return HttpResponse("Location was deleted")
    else:
        return HttpResponseBadRequest("Unable to delete a location that does not exist in the database.")

def suppliers(request):
    suppliers = list(Supplier.objects.all().values())
    suppliers_list = json.dumps(suppliers)
        
    context={
        "breadcrumb": {
                "child":"Suppliers",
                "parent":"Products"
        },
        "suppliers_list": suppliers_list
    }
    return render(request, 'inventory/suppliers.html', context)

def supplier_add(request):   
    
    sup_name = request.POST['supplier_name']
    sup_name = sup_name.capitalize()    
    contact_name = request.POST['contact_name']
    contact_email = request.POST['contact_email']
    contact_phone = request.POST['contact_phone']
    
    try:
        Supplier.objects.create(name=sup_name,
                                contact_name=contact_name,
                                contact_email=contact_email,
                                contact_phone=contact_phone)
        
        return HttpResponse("New supplier was added")
    except IntegrityError as e:
        return HttpResponseBadRequest("Supplier name already existed")

def supplier_update(request):    
    sup_id = request.POST.get('supplier_id')
    sup_name = request.POST.get('supplier_name')
    supplier = get_object_or_404(Supplier, id=sup_id)
    if supplier is not None:
        try:
            supplier.name = sup_name.capitalize()
            supplier.contact_name = request.POST['contact_name']
            supplier.contact_email = request.POST['contact_email']
            supplier.contact_phone =  request.POST['contact_phone']
            supplier.save()
            return HttpResponse("Supplier name was updated")
        except IntegrityError as e:
            return HttpResponseBadRequest("Supplier name already existed.")
    else:
        return HttpResponseBadRequest("Unable to update a supplier that does not exist in the database.")

def supplier_delete(request):
    sup_id = request.POST.get('supplier_id')
    supplier = get_object_or_404(Supplier, id=sup_id)
    if supplier is not None:
        supplier.delete()
        return HttpResponse("Supplier was deleted")
    else:
        return HttpResponseBadRequest("Unable to delete a supplier that does not exist in the database.")


@csrf_exempt
def ajax_products(request):
    if request.method == "GET":
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
    
    return JsonResponse(serializer.data, safe=False)
