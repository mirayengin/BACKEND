from rest_framework import serializers
from .models import Teacher, Lesson, Grade, Students


class TeacherSerializer(serializers.ModelSerializer):
  class Meta:
    model = Teacher
    fields = ("name",)

class LessonSerializer(serializers.ModelSerializer):
  class Meta:
    model = Lesson
    fields = ("name", "teacher")



class StudentsSerializer(serializers.ModelSerializer):
  class Meta:
    model = Students
    fields = ("first_name","last_name")



class GradeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Grade
    fields = ("grade",)