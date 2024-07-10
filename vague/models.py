from django.db import models
from datetime import datetime
from datepick import fields
from django.urls import reverse

# Create your models here.
class Vague(models.Model):
    quantity_at_the_start = models.PositiveIntegerField(max_length=4)
    start_date = fields.DateField()
    died = models.PositiveIntegerField(max_length=4, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    season = models.CharField(max_length=14)
    max_temperature = models.ValueRange(start= -70, end=70)
    
    def __str__(self):
        return f"{self.start_date.day} of the {self.start_date.month}-{self.start_date.year}"
    
    def get_absolute_url(self):
        return reverse("vague_detail", kwargs={"pk": self.pk})
    
    
    def get_the_rest(self):
        if self.died:
            return self.quantity_at_the_start - self.died
        return self.quantity_at_the_start
    
    
    