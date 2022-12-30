from rest_framework import serializers
from .models import Post,Category

class PostSerializer(serializers.ModelSerializer):
  class Meta:
    model = Post
    fields = ["title","contact"]


class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = Category
    fields = ["id", "name"]