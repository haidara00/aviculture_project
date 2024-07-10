from django.urls import path

from .views import *
urlpatterns = [
    path('',ListSupplier.as_view(), name="supplier_list"),
    path('<int:pk>/', DetailSupplier.as_view(), name="supplier_detail"),
    path('create/',CreateSupplier.as_view(), name="supplier_create"),
    path('update/<int:pk>/',UpdateSupplier.as_view(), name="supplier_update"),
    path('delete/<int:pk>/',DeleteSupplier.as_view(), name="supplier_delete"),
    
]