from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=30)
    roll = models.CharField(max_length=10)
    department = models.CharField(max_length=10)
    address = models.CharField(max_length=30)

   
