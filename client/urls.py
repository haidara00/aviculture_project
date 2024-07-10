from django.urls import path

from .views import *
urlpatterns = [
    path('',ListClient.as_view(), name="client_list"),
    path('<int:pk>/', DetailClient.as_view(), name="client_detail"),
    path('create/',CreateClient.as_view(), name="client_create"),
    path('update/<int:pk>/',UpdateClient.as_view(), name="client_update"),
    path('delete/<int:pk>/',DeleteClient.as_view(), name="client_delete"),
    
    
]
