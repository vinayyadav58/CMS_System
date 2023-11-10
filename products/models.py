from django.db import models
from django.contrib.auth.models import User
from django.utils.html import mark_safe


class Product(models.Model):
    product_name = models.CharField(max_length=100,)
    company_name = models.CharField(max_length=100)
    product_image = models.ImageField(upload_to='product_images/')
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    entered_by = models.ForeignKey(User, on_delete=models.CASCADE,default=1)

    

    def __str__(self):
        return self.product_name
    

    

