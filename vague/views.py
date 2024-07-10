from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import *

from .models import Vague

# =========== Vague CRUD ===========

class ListVague(ListView):
    model = Vague
    template_name = "vague/vague_list.html"
    queryset = Vague.objects.all()
    
class DetailVague(DetailView):
    model = Vague
    template_name = "vague/vague_detail.html"

class CreateVague(CreateView):
    model = Vague
    fields = ("start_date", "quantity_at_the_start","season", "died", )
    template_name = "vague/vague_create.html"
    success_url = reverse_lazy("vague_list")
    

class UpdateVague(UpdateView):
    model = Vague
    fields = '__all__'
    template_name = "vague/vague_update.html"

class DeleteVague(DeleteView):
    model = Vague
    template_name = "vague/vague_delete.html"
    success_url = reverse_lazy("vague_list")
