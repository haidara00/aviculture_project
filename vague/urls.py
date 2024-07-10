from django.urls import path

from .views import *


urlpatterns = [
    path('',ListVague.as_view(), name="vague_list"),
    path('<int:pk>/', DetailVague.as_view(), name="vague_detail"),
    path('create/',CreateVague.as_view(), name="vague_create"),
    path('update/<int:pk>/',UpdateVague.as_view(), name="vague_update"),
    path('delete/<int:pk>/',DeleteVague.as_view(), name="vague_delete"),
    
    
]
