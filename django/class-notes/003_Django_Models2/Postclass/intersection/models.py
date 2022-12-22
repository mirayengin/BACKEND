from django.db import models

# Create your models here.
class Student(models.Model):
  first_name = models.CharField(max_length=20)
  last_name = models.CharField(max_length=20)
  about = models.TextField(blank=True, null=True)
  number = models.PositiveSmallIntegerField(unique=True)
  create_data = models.DateTimeField(auto_now_add=True)
  update_data = models.DateTimeField(auto_now=True)


  def __str__(self):
    return f"{self.first_name} {self.last_name} {self.number}"