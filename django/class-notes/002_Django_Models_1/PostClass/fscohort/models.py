from django.db import models

class Student(models.Model):
  first_name = models.CharField(max_length=20)
  last_name = models.CharField(max_length=20)
  number = models.IntegerField(1111)
  about = models.TextField(blank=True, null=True) # blank=True ise boş bırakılabilir null=True ise null yazar boş yerlerde
  register = models. DateTimeField(auto_now_add=True) # take the create data and tıme
  last_update_date = models.DateTimeField(auto_now=True) # take the update data and tıme
  is_active = models.BooleanField()
