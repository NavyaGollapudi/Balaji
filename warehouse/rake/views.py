from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from .forms import BranchForm, CategoryForm, CustomerForm, RakeArrivalForm
from django.views.generic import (CreateView, ListView, UpdateView, DeleteView, TemplateView)
from .models import Category, Customer, Branch, RakeArrival
from bootstrap_modal_forms.generic import BSModalCreateView, BSModalUpdateView

# Create your views here.

class WelcomePageView(TemplateView):
    template_name = 'base.html'

# Category Views 
class CategoryCreateView(BSModalCreateView):
    form_class = CategoryForm
    model = Category 
    template_name = 'category_create.html'
    success_url = reverse_lazy('category_list')

    def form_valid(self, form):        
        if not self.request.headers.get('x-requested-with') == 'XMLHttpRequest':

            obj = form.save()
        
        return super().form_valid(form)    

class CategoryListView(ListView):
    model = Category
    template_name = 'category_list.html'
    
    def get_queryset(self):
        return Category.objects.all().order_by('id')
    
class CategoryUpdateView(BSModalUpdateView):
    form_class = CategoryForm
    model = Category 
    template_name = 'category_edit.html'
    success_url = reverse_lazy('category_list')
    
class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'category_delete.html'
    success_url = reverse_lazy('category_list')
    
# Customer Views
class CustomerCreateView(BSModalCreateView):
    form_class = CustomerForm
    model = Customer
    template_name = 'customer_create.html'
    success_url = reverse_lazy('customer_list')
    
class CustomerListView(ListView):
    model = Customer
    template_name = 'customer_list.html'
    
    def get_queryset(self):
        return Customer.objects.all().order_by('id')
    
class CustomerUpdateView(UpdateView):
    form_class = CustomerForm
    model = Customer
    template_name = 'customer_create.html'
    success_url = reverse_lazy('customer_list')
    
class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = 'customer_delete.html'
    success_url = reverse_lazy('customer_list')
    
# Branch Views
class BranchCreateView(CreateView):
    form_class = BranchForm
    model = Branch
    template_name = 'branch_create.html'
    success_url = reverse_lazy('branch_list')
    
class BranchListView(ListView):
    model = Branch
    template_name = 'branch_list.html'
    
    def get_queryset(self):
        return Branch.objects.all().order_by('id')
    
class BranchUpdateView(UpdateView):
    form_class = BranchForm
    model = Branch
    template_name = 'branch_create.html'
    success_url = reverse_lazy('branch_list')
    
class BranchDeleteView(DeleteView):
    model = Branch
    template_name = 'branch_delete.html'
    success_url = reverse_lazy('branch_list')
    
# Rake Arrival 
class RakeArrivalCreateView(CreateView):
    form_class = RakeArrivalForm
    model = RakeArrival
    template_name = 'rake_create.html'
    success_url = reverse_lazy('rake_list')
    
class RakeArrivalListView(ListView):
    model = RakeArrival
    template_name = 'rake_list.html'
    
    def get_queryset(self):
        return RakeArrival.objects.all().order_by('id')
    
class RakeArrivalUpdateView(UpdateView):
    form_class = RakeArrivalForm
    model = RakeArrival
    template_name = 'rake_create.html'
    success_url = reverse_lazy('rake_list')
    
class RakeArrivalDeleteView(DeleteView):
    model = RakeArrival
    template_name = 'rake_delete.html'
    success_url = reverse_lazy('rake_list')




    
    
    
    
