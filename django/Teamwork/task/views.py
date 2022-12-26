from django.shortcuts import render, HttpResponse,get_list_or_404
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
def get_artist_list(request):
  artists = Artist.objects.all()
  seriliazer = ArtistSerializer(artists, many=True)
  return Response(seriliazer.data)


@api_view(["GET"])
def artist_detail(request, pk ):
  # artists = Artist.objects.get(id=pk)
  artists = get_list_or_404(Artist, id=pk)
  seriliazer = ArtistSerializer(artists)
  return Response(seriliazer.data)










@api_view(["POST"])
def post_artist_list(request):
  serializer = ArtistSerializer(data=request.data)
  if serializer.is_valid():
    serializer.save()
    message = {
      "message": "Artist  saved successfully!"
    }
    return Response(message, status=status.HTTP_201_CREATED)
  return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


@api_view(["GET", "POST"])
def artist_list(request):
  if(request.method == "GET"):
    artists = Artist.objects.all()
    seriliazer = ArtistSerializer(artists, many=True)
    return Response(seriliazer.data)
  elif(request.method == "GET"):
    serializer = ArtistSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      message = {
      "message": "Artist  saved successfully!"
    }
      return Response(message, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


@api_view(["PUT"])
def artist_update(request,pk):
  artist = get_list_or_404(Artist, id=pk)
  seriliazer = ArtistSerializer(instance=artist, data=request.data)
  if seriliazer.is_valid():
    seriliazer.save()
    message = {
      "message" : "Updated Put"
    }
    return Response(seriliazer.data, status=status.HTTP_201_CREATED)
  return Response(seriliazer.error, status=status.HTTP_400_BAD_REQUEST)



@api_view(["DELETE"])
def artist_delete(request,pk):
  artist = get_list_or_404(Artist, id=pk)
  artist.delete()
  message = {
      "message" : "Artist DELETE"
    }
  return Response(message)



@api_view(["DELETE","PUT"])
def artist_update_delete(request, pk):
  if request.metod == "PUT":
    artist = get_list_or_404(Artist, id=pk)
    seriliazer = ArtistSerializer(instance=artist, data=request.data)
    if seriliazer.is_valid():
      seriliazer.save()
      message = {
        "message" : "Updated Put"
      }
      return Response(seriliazer.data, status=status.HTTP_201_CREATED)
    return Response(seriliazer.error, status=status.HTTP_400_BAD_REQUEST)
  elif request.metod == "PUT":
    artist = get_list_or_404(Artist, id=pk)
    artist.delete()
    message = {
      "message" : "Artist DELETE"
    }
    return Response(message)