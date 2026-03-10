from django.db import models

# Create your models here.

class contactUs(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    message = models.TextField()