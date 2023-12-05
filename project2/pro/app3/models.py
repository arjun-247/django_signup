from django.db import models

# Create your models here.
class database1(models.Model):   
    name=models.CharField(max_length=255)
    username=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
