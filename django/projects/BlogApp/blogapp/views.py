from django.shortcuts import render

from .serializers import PostSerializer,CategorySerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Post, Category


from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view,action

# Create your views here.

class CategoryCVS(ListCreateAPIView):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer

class CategoryDetailCVS(RetrieveUpdateDestroyAPIView):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer


# class CategoryCreateCVS(CreateAPIView):
#   queryset = Category.objects.all()
#   serializer_class = CategorySerializer


class PostMVS(ModelViewSet):

    queryset=Post.objects.all()
    serializer_class = PostSerializer

    # @action(detail=False, methods=["GET"])
    # def student_count(self, request):
    #     count={
    #         "student-count": self.queryset.count()
    #     }
    #     return Response(count)


