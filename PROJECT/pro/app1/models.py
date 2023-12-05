from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=25)
    age=models.IntegerField()

class employee(models.Model):
    emp_id=models.IntegerField()
    emp_name=models.CharField(max_length=25)
    emp_salary=models.IntegerField()
    designation=models.CharField(max_length=25)
    place=models.CharField(max_length=25)