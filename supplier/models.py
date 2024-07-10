from django.db import models
from django.urls import reverse, reverse_lazy

# Create your models here.
class Supplier(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.PositiveIntegerField(null=True, blank=True)
    email = models.EmailField(max_length=254,null=True, blank=True)
    credit = models.DecimalField( max_digits=10, decimal_places=2,null=True, blank=True)
    paid_off = models.DecimalField(max_digits=10, decimal_places=2)
    is_male = models.BooleanField(default=None, null=True, blank=True)
    
    
    def __str__(self):
        return self.first_name.title() + " " + self.last_name.upper()
    
    def get_absolute_url(self):
        return reverse("supplier_detail", kwargs={"pk": self.pk})
    
    def get_the_rest_of_credit(self):
        
        self.result =  self.credit - self.paid_off
        if self.result > 0:
            return f"Il vous rest {self.result}"
        elif self.result <  0:
            return f"Vous avez {-(self.result)}Fcfa chez {self.first_name.title()} comme avance"
        return f"Compte soldé"
    def get_gender(self):
        if self.is_male:
            return "Masculin"
        elif self.is_male == False:
            return "Feminin"
        return "Inconnu"
    