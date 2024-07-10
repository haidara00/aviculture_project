from django.forms import ModelForm

from .models import Supplier

class PayOffForm(ModelForm):
    
    class Meta:
        model = Supplier
        fields = ("paid_off",)