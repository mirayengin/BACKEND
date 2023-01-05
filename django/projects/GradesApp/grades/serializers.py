from rest_framework import serializers
from .models import Teacher, Lesson, Grade, Students


class TeacherSerializer(serializers.ModelSerializer):
  model = Teacher
  fields = ["name"]

class LessonSerializer(serializers.ModelSerializer):
  model = Lesson
  fields = ["name", "teacher"]



class StudentsSerializer(serializers.ModelSerializer):
  model = Students
  fields = ["first_name","last_name"]



class GradeSerializer(serializers.ModelSerializer):
  model = Grade
  fields = ["grade"]