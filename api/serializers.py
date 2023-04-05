from rest_framework import serializers
from main.models import Customer
from inventory.models import Product, Category, Unit
from order.models import Order

class ProductSerializer(serializers.ModelSerializer):
  category = serializers.CharField(read_only=True, source="category.name")
  
  class Meta:
      model = Product
      fields = "__all__"

class UnitSerializer(serializers.ModelSerializer):    
  class Meta:
      model = Unit
      fields = "__all__"

class CustomerSerializer(serializers.Serializer):
   id = serializers.IntegerField()
   customer_name = serializers.CharField(max_length=150)
   address1 = serializers.CharField(max_length=150, allow_blank=True )
   address2 = serializers.CharField(max_length=150, allow_blank=True)
   city =serializers.CharField(max_length=100, allow_blank=True)
   province =serializers.CharField(max_length=150, allow_blank=True)
   zipcode = serializers.CharField(max_length=20, allow_blank=True)
   contact_email = serializers.EmailField()
   contact_no = serializers.CharField(max_length=50)
   salesman_name = serializers.CharField(max_length=20, allow_blank=True)
   is_active= serializers.BooleanField(default=True)
   created_on =serializers.DateTimeField()
   updated_on =serializers.DateTimeField()
   
  
class CategorySerializer(serializers.ModelSerializer):
   class Meta:
      model = Category
      fields = "__all__"

class OrderSerializer(serializers.ModelSerializer):
   class Meta:
      model = Order
      fields =  ["id",
        "order_no",
        "order_date",
        "po_no",
        "order_amount",
        "vat_amount",
        "net_amount",
        "payment_status",
        "order_status",
        "salesman_name",
        "customer_name",
        "user"
      ]