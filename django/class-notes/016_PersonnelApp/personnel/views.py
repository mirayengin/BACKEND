from django.shortcuts import render
from .serializers import DepartmentSerializer,PersonnelSerializer
from .models import Department,Personnel,Department
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .permissions import IsStafforReadOnly



class DepartmentView(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [IsAuthenticated,IsStafforReadOnly]



class PersonnelView(generics.ListCreateAPIView):
    queryset = Personnel.objects.all()
    serializer_class = PersonnelSerializer
    