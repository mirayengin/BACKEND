from rest_framework import serializers
from .models import Teacher, Lesson, Grade, Students

class GradeSerializer(serializers.ModelSerializer):
  student = serializers.StringRelatedField()
  lesson = serializers.StringRelatedField()
  class Meta:
    model = Grade
    fields = ("grade","student","lesson")
class TeacherSerializer(serializers.ModelSerializer):
  class Meta:
    model = Teacher
    fields = ("name",)

class LessonSerializer(serializers.ModelSerializer):
  lesson_grades = GradeSerializer(many=True)
  class Meta:
    model = Lesson
    fields = ("name", "teacher","lesson_grades")



class StudentsSerializer(serializers.ModelSerializer):
  student_grades = GradeSerializer(many=True)
  class Meta:
    model = Students
    fields = ("number","first_name","last_name","student_grades")



