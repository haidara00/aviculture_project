from django.db import models

from vague.models import Vague
from client.models import Client

#  le client, le nombre de poulet, le prix, la vague à la quelle l'achat à été éffectué;
# 
# 
# 
class Contract(models.Model):
    vague = models.ForeignKey(Vague, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    
    def __str__(self):
        return f"{self.client.first_name}: {self.price}Fcfa"
    