from rest_framework.viewsets import ModelViewSet

from .models import Category, Blog
from .serializers import CategorySerializer, BlogSerializer

# from django_filters.rest_framework import DjangoFilterBackend


class CategoryView(ModelViewSet):  # crud
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filterset_fields = ["name"]

    # filter_backends = [DjangoFilterBackend]



class BlogView(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    filterset_fields = ["category_id"]
    search_fields = ["title","content"]
    # fieldsets_fields = ["category__name"] #? name e göre filter
