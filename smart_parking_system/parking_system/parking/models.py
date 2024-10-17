from django.db import models

# Create your models here.

class Vehicle(models.Model):
    vehicle_number = models.CharField(max_length=15)
    entry_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.vehicle_number
    
