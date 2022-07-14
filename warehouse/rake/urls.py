from django.urls import path
from rake import views
from .views import (CategoryCreateView, CategoryUpdateView, CategoryDeleteView, CategoryListView)
from .views import (CustomerCreateView,CustomerListView,CustomerUpdateView,CustomerDeleteView)
from .views import (BranchCreateView, BranchUpdateView, BranchDeleteView, BranchListView)
from .views import(RakeArrivalListView,RakeArrivalDeleteView, RakeArrivalCreateView, RakeArrivalUpdateView)


urlpatterns = [
    path('',views.WelcomePageView.as_view(),name ='welcome_page'),
    # category 
    path('category/create',views.CategoryCreateView.as_view(),name ='category_create'),
    path('category/list',views.CategoryListView.as_view(),name ='category_list'),
    path('category/edit/<int:pk>',views.CategoryUpdateView.as_view(),name ='category_edit'),
    path('category/delete/<int:pk>',views.CategoryDeleteView.as_view(),name ='category_delete'),
    # customer
    path('customer/create',views.CustomerCreateView.as_view(),name ='customer_create'),
    path('customer/list',views.CustomerListView.as_view(),name ='customer_list'),
    path('customer/edit/<int:pk>',views.CustomerUpdateView.as_view(),name ='customer_edit'),
    path('customer/delete/<int:pk>',views.CustomerDeleteView.as_view(),name ='customer_delete'),
    # branch
    path('branch/create',views.BranchCreateView.as_view(),name ='branch_create'),
    path('branch/edit/<int:pk>',views.BranchUpdateView.as_view(),name ='branch_edit'),
    path('branch/delete/<int:pk>',views.BranchDeleteView.as_view(),name ='branch_delete'),
    path('branch/list',views.BranchListView.as_view(),name ='branch_list'),
    # rake
    path('rake/create',views.RakeArrivalCreateView.as_view(),name ='rake_create'),
    path('rake/edit/<int:pk>',views.RakeArrivalUpdateView.as_view(),name ='rake_edit'),
    path('rake/delete/<int:pk>',views.RakeArrivalDeleteView.as_view(),name ='rake_delete'),
    path('rake/list',views.RakeArrivalListView.as_view(),name ='rake_list'),
]
