from rest_framework import serializers
from main.models import Customer
from inventory.models import Product, Category, Unit,Inventory
from order.models import Order

class ProductSerializer(serializers.ModelSerializer):
  category = serializers.CharField(read_only=True, source="category.name")
  
  class Meta:
      model = Product
      fields = "__all__"

class ProductInventorySerializer(serializers.ModelSerializer):
   sku = serializers.CharField(read_only=True, source="product.sku")
   name = serializers.CharField(read_only=True, source="product.name")
   location = serializers.CharField(read_only=True, source="location.name")
   category = serializers.CharField(read_only=True, source="product.category.name")   
   barcode = serializers.CharField(read_only=True, source="product.barcode")
   unit =serializers.CharField(read_only=True, source="product.unit")
   retail_price = serializers.FloatField(source="product.retail_price")
   purchased_price = serializers.FloatField(source="product.purchased_price")
   image = serializers.ImageField(source="product.image")
   tax = serializers.IntegerField(source="product.tax")
   brand = serializers.CharField(source="product.brand")
   is_active= serializers.BooleanField(source="product.is_active")
   created_on =serializers.DateTimeField(source="product.created_on")
   updated_on =serializers.DateTimeField(source="product.updated_on")
   supplier = serializers.IntegerField(source="product.supplier_id")
   user = serializers.IntegerField(source="product.user_id")
   
   class Meta:
      model = Inventory
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