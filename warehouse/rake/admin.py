from django.contrib import admin
from .models import Branch, Customer, Category, RakeArrival


# Register your models here.
admin.site.register(Customer)
admin.site.register(Category)
admin.site.register(Branch)
admin.site.register(RakeArrival)