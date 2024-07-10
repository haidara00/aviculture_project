from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import *

from .models import Client

# ======== Client CRUD ===========

class ListClient(ListView):
    model = Client
    template_name = "client/client_list.html"
    queryset = Client.objects.all()
    
class DetailClient(DetailView):
    model = Client
    template_name = "client/client_detail.html"

class CreateClient(CreateView):
    model = Client
    fields = "__all__"
    template_name = "client/client_create.html"
    success_url = reverse_lazy("client_list")
    

class UpdateClient(UpdateView):
    model = Client
    fields = '__all__'
    template_name = "client/client_update.html"

class DeleteClient(DeleteView):
    model = Client
    template_name = "client/client_delete.html"
    success_url = reverse_lazy("client_list")
