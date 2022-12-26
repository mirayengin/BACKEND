from django.shortcuts import render, HttpResponse
from .models import (
  Artist,
  Song,
  Album,
  Lyric
)
from .serializer import (
  ArtistSerializer,
  AlbumSerializer,
  LyricSerializer,
  SongSerializer
)
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
# def artist_list(request):
#   return HttpResponse("Welcome TASK page")

@api_view(["GET"])
def artistList(request):
  artists = Artist.objects.all()
  seriliazer = ArtistSerializer(artists, many=True)
  return Response(seriliazer.data)
