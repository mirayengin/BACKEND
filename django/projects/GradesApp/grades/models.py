from django.db import models

# Create your models here.
class Teacher(models.Model):
  name = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  class Meta:
    verbose_name = "Ogretmen"



class Lesson(models.Model):
  name = models.CharField(max_length=20)
  teacher = models.OneToOneField(Teacher, on_delete=models.CASCADE)

  def __str__(self):
    return f'{self.name}, {self.teacher}'

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
  lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name="lesson_grades")
  student = models.ForeignKey(Students, on_delete=models.CASCADE, related_name="student_grades")
  grade = models.IntegerField()


  def __str__(self):
    return f'{str(self.grade)} {self.lesson} {self.student}'

  class Meta:
    verbose_name = "Notlar"