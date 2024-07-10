from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import *

from .models import Supplier

# ======== Supplier CRUD ======
class ListSupplier(ListView):
    model = Supplier
    template_name = "supplier/supplier_list.html"
    queryset = Supplier.objects.all()
    
class DetailSupplier(DetailView):
    model = Supplier
    template_name = "supplier/supplier_detail.html"

class CreateSupplier(CreateView):
    model = Supplier
    fields = "__all__"
    template_name = "supplier/supplier_create.html"
    success_url = reverse_lazy("supplier_list")
    

class UpdateSupplier(UpdateView):
    model = Supplier
    
    fields = "__all__"
    template_name = "supplier/supplier_update.html"

class DeleteSupplier(DeleteView):
    model = Supplier
    template_name = "supplier/supplier_delete.html"
    success_url = reverse_lazy("supplier_list")
