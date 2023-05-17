from django.http import HttpResponseBadRequest, JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from rest_framework import viewsets, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.mixins import UpdateModelMixin
from rest_framework import status
from .serializers import ProductSerializer,ProductInventorySerializer, CustomerSerializer, CategorySerializer
from .serializers import OrderSerializer, UnitSerializer, InventorySerializer
from inventory.models import Product,Category, Unit, Inventory
from order.models import Order
from main.models import Customer
from main.functions import debug_esc


# Create your views here.

class ProductsViewSet(viewsets.ModelViewSet):
    queryset =Product.objects.all().select_related('category')
    serializer_class = ProductSerializer

class ProductsInventoryViewSet(generics.ListAPIView):
    serializer_class = ProductInventorySerializer
    lookup_url_kwarg = "location"

    def get_queryset(self):
        location_id = self.kwargs.get(self.lookup_url_kwarg)
        if location_id:
            products = Inventory.objects.all().select_related('product')
            queryset = products.filter(location=location_id)                                    
            return queryset       

class UpdateInventoryViewSet(generics.UpdateAPIView,UpdateModelMixin):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    http_method_names = ['patch',]
    lookup_field  = "pk"
       
    def partial_update(self, request, *args, **kwargs):
        object = self.get_object()       
        serializer = self.serializer_class(instance=object, 
                                           data=request.data, 
                                           partial=True)
        if serializer.is_valid():           
            serializer.save()  
            return Response(data=serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class UnitsViewSet(viewsets.ModelViewSet):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer

class OrdersViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        
        date_from = self.request.query_params.get('date-from')
        date_to = self.request.query_params.get('date-to')

        if date_from and date_to:
            queryset = queryset.filter(order_date__range=(date_from,date_to))
        
        return queryset


@csrf_exempt
def api_customers(request):
    if request.method == "GET":

        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        
        return JsonResponse(serializer.data, safe=False)
    
@csrf_exempt
def api_customer(request, id):
    try:
        customer = Customer.objects.get(pk=id)
    except Customer.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == "GET":
        serializer = CustomerSerializer(customer)
        return JsonResponse(serializer.data)
    

################### API Views #########################
