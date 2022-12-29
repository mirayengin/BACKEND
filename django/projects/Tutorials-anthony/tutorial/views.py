from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import Tutorial
from .serializer import TutorialSerializer

from .pagination import  (
  CustomPageNumberPagination,
  CustomLimitOffsetPagination,
  CustomCursorPagination
)


# from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.

class TutorialMVS(ModelViewSet):
  queryset = Tutorial.objects.all()
  serializer_class = TutorialSerializer

  #?pagination
  # pagination_class = CustomPageNumberPagination
  # pagination_class = CustomLimitOffsetPagination
  pagination_class = CustomCursorPagination

  #?filter
  # filter_backends = [DjangoFilterBackend]
  filterset_fields = ['id','title']
  search_fields = ['title']
  