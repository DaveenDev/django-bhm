from django.db import models
from django.contrib.auth.models import User
from main.models import Salesman, Customer
from inventory.models import Product
import datetime


# Create your models here.
class Order(models.Model):
    order_no = models.CharField(max_length=20, unique=True, blank=True)    
    order_date = models.DateField()
    po_no = models.CharField(max_length=30, null=True, blank=True)
    order_amount = models.FloatField()
    vat_amount  = models.FloatField()
    net_amount  = models.FloatField()
    payment_status=models.CharField(max_length=30, default="paid")
    order_status= models.CharField(max_length=30, default="new")
    salesman = models.ForeignKey(Salesman, on_delete=models.SET_NULL, null=True, blank=True)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    user = models.ForeignKey(User,on_delete=models.SET_NULL, null=True, blank=True)
    created_on =models.DateTimeField(auto_now=True, null=True)
    updated_on =models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.order_no}"
    
    def save(self, *args, **kwargs):
        
        vat = float(self.order_amount) * 0.12
        net = float(self.order_amount) - vat
        self.vat_amount = vat
        self.net_amount = net
        super(Order, self).save(*args, **kwargs)
    
    @property
    def salesman_name(self):
        return self.salesman.fullname

    @property
    def customer_name(self):
        return self.customer.customer_name
    
    @property
    def orderid(self):
        return self.id

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.DO_NOTHING, null=True, blank=True)
    price = models.FloatField()
    quantity = models.IntegerField()
    discount_amount = models.FloatField()
    line_total =models.FloatField()


class OrderDBView(models.Model):
    order_no = models.CharField(max_length=20)    
    order_date = models.DateField()
    po_no = models.CharField(max_length=30)
    tra_no = models.CharField(max_length=30)
    order_amount = models.FloatField()
    customer = models.CharField(max_length=150) 

    class Meta:
        managed = False
        db_table = "orders_view"
