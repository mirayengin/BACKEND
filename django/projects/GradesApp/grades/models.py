from django.db import models

# Create your models here.
class Teacher(models.Model):
  name = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  class Meta:
    verbose_name = "Ögretmen"



class Lesson(models.Model):
  name = models.CharField(max_length=20)
  teacher = models.OneToOneField(Teacher, on_delete=models.CASCADE)

  def __str__(self):
    return self.name

  class Meta:
    verbose_name = "Dersler"




class Students(models.Model):
  number = models.IntegerField()
  first_name = models.CharField(max_length=25)
  last_name = models.CharField(max_length=25)


  def __str__(self):
    return f'{self.first_name} {self.last_name}'

  class Meta:
    verbose_name = "Ogrenci"



class Grade(models.Model):
  lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
  student = models.ForeignKey(Students, on_delete=models.CASCADE)
  grade = models.IntegerField()


  def __str__(self):
    return str(self.grade)

  class Meta:
    verbose_name = "Notlar"