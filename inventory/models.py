from django.db import models
from django.contrib.auth.models import User

# Create your models here.
    
class Category(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Categories"

class Supplier(models.Model):
    name = models.CharField(max_length=100)
    contact_name = models.CharField(max_length=100,null=True,blank=True)
    contact_email = models.EmailField(null=True,blank=True)
    contact_phone = models.TextField(null=True,blank=True)

class Unit(models.Model):
    unit = models.CharField(max_length=20)

class Product(models.Model):
    sku = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=150)
    barcode = models.CharField(max_length=100,null=True)
    unit =models.CharField(max_length=20)
    retail_price = models.FloatField()
    purchased_price = models.FloatField()
    image = models.ImageField(upload_to="product-images", null=True, blank=True)
    tax = models.IntegerField(null = True)
    brand = models.CharField(max_length=50, null=True, blank=True)
    category=models.ForeignKey(Category,on_delete=models.SET_NULL, null=True, blank=True)
    is_active= models.BooleanField(default=True),
    created_on =models.DateTimeField(auto_now=True, null=True)
    updated_on =models.DateTimeField(null=True, blank=True)
    supplier = models.ForeignKey(Supplier, on_delete= models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name
    
    @property
    def category_name(self):
        return self.category.name
    

class InvLocation(models.Model):
    name = models.CharField(max_length=30)
    address1 = models.CharField(max_length=150)
    address1 = models.CharField(max_length=150)
    city = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    post_code = models.CharField(max_length=50)
    country = models.CharField(max_length=100)

class Inventory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    stock_level = models.IntegerField()
    bin_rack = models.CharField(max_length=20,null=True,blank=True)
    location = models.ForeignKey(InvLocation, on_delete=models.CASCADE)


