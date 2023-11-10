from django.db import models

# Create your models here.

from django.db import models

class deatil_emp(models.Model):
        activity_status = (("Active","Active"),("Inactive","Inactive"))
        first_name = models.CharField(max_length=100)
        last_name = models.CharField(max_length=100)
        email = models.EmailField(max_length=100)
        joining = models.DateField()
        status = models.CharField(max_length=30,choices=activity_status)

