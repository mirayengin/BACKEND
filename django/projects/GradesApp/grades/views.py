from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import TeacherSerializer, LessonSerializer, StudentsSerializer, GradeSerializer
from .models import Teacher,Lesson,Students,Grade

class TeacherMVS(ModelViewSet):
  queryset= Teacher.objects.all()
  serializer_class = TeacherSerializer

class LessonMVS(ModelViewSet):
  queryset= Lesson.objects.all()
  serializer_class = LessonSerializer

class StudentsMVS(ModelViewSet):
  queryset= Students.objects.all()
  serializer_class = StudentsSerializer

class GradeMVS(ModelViewSet):
  queryset= Grade.objects.filter()
  serializer_class = GradeSerializer
