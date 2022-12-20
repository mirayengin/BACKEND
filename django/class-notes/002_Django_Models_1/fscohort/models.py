from django.db import models

# Create your models here.
class Student(models.Model):
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  number = models.IntegerField(default=1111)
  about = models.TextField(blank=True, null=True)
  register = models.DateTimeField(auto_now_add=True) # take the createion date and tıme
  last_updated_date = models.DateTimeField(auto_now=True) # take update date and tıme
  is_active = models.BooleanField()



  def __str__(self):
    return f"{self.first_name}  {self.last_name}"

  class Meta:
    ordering = ["number"]
    verbose_name_plural = "Student_list"


  def student_year_status(self):
    import datetime
    if self.register_date < datetime.date(2019, 1, 1):
      return "Senior"
    if self.register_date < datetime.date(2020, 1, 1):
      return "Junior"
    else:
      return "Freshman"


# student.obfects.all()
# student.obfects.get(......)
# student.obfects.filter(......)

  