from django.shortcuts import render

from .serializers import PostSerializer,CategorySerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Post, Category


from rest_framework.viewsets import ModelViewSet
# from rest_framework.decorators import api_view,action

from rest_framework.permissions import BasePermission,IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly

# Create your views here.

class IsAdminUserOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in ['GET']:
            return True
        else:
            return request.user.is_staff

class CategoryCVS(ListCreateAPIView):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer
  filterset_fields = ['name']
  search_fields = ['name']
  ordering_fields = ['id']
  permission_classes = [IsAdminUserOrReadOnly]  #! Dmin olan herşeyi olmayan yanlız get işlemini yapar


class CategoryDetailCVS(RetrieveUpdateDestroyAPIView):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer
  permission_classes = [IsAdminUser]



# class CategoryCreateCVS(CreateAPIView):
#   queryset = Category.objects.all()
#   serializer_class = CategorySerializer


class PostMVS(ModelViewSet):

    queryset=Post.objects.all()
    serializer_class = PostSerializer
    #! burda neye göre yapacağinı yazıyoruz 
    filterset_fields = ['title']
    search_fields = ['category']
    ordering_fields = ['category']

    permission_classes = [IsAuthenticatedOrReadOnly]  #! #! Giriş yapan herşeyi olmayan yanlız get işlemini yapar

    # @action(detail=False, methods=["GET"])
    # def student_count(self, request):
    #     count={
    #         "student-count": self.queryset.count()
    #     }
    #     return Response(count)


