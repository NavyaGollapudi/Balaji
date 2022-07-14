from unicodedata import name
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=256, unique = True, blank = False)
    
    def __str__(self):
        return self.name
    
class Customer(models.Model):
    name = models.CharField(max_length=256, blank = False)
    address = models.CharField(max_length=256)
    state = models.CharField(max_length=100,blank=False)
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return self.name

class Branch(models.Model):
    name = models.CharField(max_length=255,unique=True, blank = False)
    address = models.CharField(max_length=255)
    state = models.CharField(max_length=100,blank = False)
    email  = models.EmailField(unique=True)
    
    
    def __str__(self):
        return self.name

class RakeArrival(models.Model):
    rrdate = models.DateField(blank = False)
    rrnumber = models.CharField(max_length = 256, blank = False)
    receivingdate = models.DateField(blank = False)
    customer_name = models.ForeignKey(Customer, verbose_name = ("Customers"), on_delete =models.CASCADE)
    category_name = models.ForeignKey(Category, on_delete = models.CASCADE)
    product_description = models.CharField(max_length =100, blank = False)
    quantity = models.DecimalField(max_digits = 10, decimal_places = 2, blank = False)
    bags_count = models.PositiveIntegerField(blank = False)
    receiving_branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.rrnumber)