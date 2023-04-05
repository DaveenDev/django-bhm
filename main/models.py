from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Salesman(models.Model):
    fullname = models.CharField(max_length=100, unique=True)
    contact_email = models.EmailField()
    contact_no=models.CharField(max_length=50)
    created_on= models.DateField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    is_active= models.BooleanField(default=True),
    created_on =models.DateTimeField(auto_now=True, null=True)
    updated_on =models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name_plural="Salesmen"

    def __str__(self):
        return self.fullname

class Customer(models.Model):
    customer_name = models.CharField(max_length=150, unique=True)
    address1 = models.CharField(max_length=150, null=False, blank=False )
    address2 = models.CharField(max_length=150, null=True, blank=True)
    city =models.CharField(max_length=100, null=False, blank=False)
    province =models.CharField(max_length=150, null=False, blank=False)
    zipcode = models.CharField(max_length=20, null=False, blank=False)
    contact_email = models.EmailField(blank=True)
    contact_no = models.CharField(max_length=50, blank=True)
    salesman = models.ForeignKey(Salesman,on_delete=models.SET_NULL, null=True, blank=True)
    is_active= models.BooleanField(default=True),
    created_on =models.DateTimeField(auto_now=True, null=True, blank=True)
    updated_on =models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.customer_name
    
    @property
    def salesman_name(self):
        return self.salesman.fullname


    

