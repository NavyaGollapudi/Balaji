from django import forms
from .models import Category, Customer, Branch, RakeArrival
from bootstrap_modal_forms.forms import BSModalModelForm

class CategoryForm(BSModalModelForm):
    
    class Meta():
        model = Category
        fields = "__all__"
        
class CustomerForm(BSModalModelForm):
    
    class Meta():
        model = Customer
        fields = "__all__"
        
class BranchForm(forms.ModelForm):
    
    class Meta():
        model = Branch
        fields = "__all__"
        
class RakeArrivalForm(forms.ModelForm):
    
    class Meta():
        model = RakeArrival
        fields = "__all__"