from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Category, Blog
from .serializers import CategorySerializer, BlogSerializer
from .permissions import IsAdminOrReadOnly

# from django_filters.rest_framework import DjangoFilterBackend


class CategoryView(ModelViewSet):  # crud
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filterset_fields = ["name"]
    permission_classes = [IsAdminOrReadOnly]

    # filter_backends = [DjangoFilterBackend]



class BlogView(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    filterset_fields = ["category_id"]
    search_fields = ["title","content"]
    permission_classes = [IsAuthenticatedOrReadOnly]
    # fieldsets_fields = ["category__name"] #? name e göre filter
