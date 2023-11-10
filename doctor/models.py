from django.db import models
from django.contrib.auth.models import User
from products.models import Product



# Create your models here.

class Doctor(models.Model):
    SPECIALISATION_CHOICES = [
        ('Chest', 'Chest'),
        ('Heart', 'Heart'),
        ('General', 'General'),
        ('Orthopaedic', 'Orthopaedic'),
        # Add more choices for other specialisations
    ]

    doctor_name = models.CharField(max_length=100)
    specialisation = models.CharField(max_length=50, choices=SPECIALISATION_CHOICES)
    contact_number = models.CharField(max_length=20)
    location = models.CharField(max_length=100)
    entered_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.doctor_name
    

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    entered_by = models.ForeignKey(User, on_delete=models.CASCADE)

    
    def __str__(self):
        return f"{self.doctor} - {self.date} {self.time}"

class Deal(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    product_name = models.ForeignKey(Product, on_delete=models.CASCADE)
    # product_name = models.CharField(max_length=100)
    quantity_ordered = models.PositiveIntegerField()
    entered_by = models.ForeignKey(User, on_delete=models.CASCADE)
