from django.db import models

# Create your models here.

class Student(models.Model):
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  #? Field lerde blank=True kullandığımız zaman bunları boş bırakarakta data oluşturabiliriz  
  number = models.IntegerField(blank=True, null=True)
  age = models.IntegerField()
  
def __str__(self):
  return self.first_name


  