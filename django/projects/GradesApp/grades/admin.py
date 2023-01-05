from django.contrib import admin
from .models import Teacher, Lesson, Grade, Students
# Register your models here.


admin.site.register(Teacher)
admin.site.register(Lesson)
admin.site.register(Grade)
admin.site.register(Students)