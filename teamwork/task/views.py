from rest_framework.decorators import api_view,action
from rest_framework.views import APIView
from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import (
  Artist,
  Album,
  Song,
  Lyric
)

from .serializer import (
  AlbumSerializer,
  ArtistSerializer,
  SongSerializer,
  LyricSerializer,
  SongLyricSerializer
)
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import mixins,GenericAPIView,ListCreateAPIView, RetrieveUpdateDestroyAPIView

# Create your views here.
# def artist_list(request):
#   return HttpResponse("Welcome TASK page")

@api_view(['GET'])
def get_artist_list(request):
  artists = Artist.objects.all()
  serializer = ArtistSerializer(artists, many=True)
  return Response(serializer.data)

@api_view() #default get
def artist_detail(request, pk):
  # artist = Artist.objects.get(id=pk)
  artist = get_object_or_404(Artist, id=pk)
  serializer = ArtistSerializer(artist)
  return Response(serializer.data)

@api_view(['POST'])
def post_artist_list(request):
  serializer = ArtistSerializer(data=request.data)
  if serializer.is_valid():
    serializer.save()
    message = {
      "message" : "Updated POST"
    }
    # return Response(serializer.data)
    return Response(message, status=status.HTTP_201_CREATED)
  return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    
@api_view(['GET', 'POST'])
def artist_list(request):
  if request.method == 'GET':
    artists = Artist.objects.all()
    serializer = ArtistSerializer(artists, many=True)
    return Response(serializer.data)
  elif request.method == 'POST':
    serializer = ArtistSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      message = {
      "message" : "Updated POST"
    }
      return Response(message, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
  
@api_view(['PUT'])
def artist_update(request, pk):
  artist = get_object_or_404(Artist, id=pk)
  serializer = ArtistSerializer(instance=artist, data=request.data)
  if serializer.is_valid():
    serializer.save()
    message = {
      "message" : "Updated PUT"
    }
    return Response(message, status=status.HTTP_201_CREATED)
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def artist_delete(request, pk):
  artist = get_object_or_404(Artist, id=pk)
  artist.delete()
  message = {
      "message" : "Artist DELETED"
    }
  return Response(message)

@api_view(['PUT', 'DELETE'])
def artist_update_delete(request, pk):

  if request.method == 'PUT':
    artist = get_object_or_404(Artist, id=pk)
    print(artist)
    serializer = ArtistSerializer(instance=artist, data=request.data)
    if serializer.is_valid():
      serializer.save()
      message = {
      "message" : "Artist Updated"
    }
      return Response(message, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  elif request.method == 'DELETE':
    artist = get_object_or_404(Artist, id=pk)
    artist.delete()
    message = {
        "message" : "Artist DELETED"
      }
    return Response(message)

@api_view()  
def song_lyric(request):
  detail_song = Song.objects.all()
  serializer = SongLyricSerializer(detail_song, many=True)
  return Response(serializer.data)


  #!######################### CLASS BASED VIEWS ###########################

#! API_VIEW

class ArtistListCreate(APIView):

  def get(self,request):
    artists = Artist.objects.all()
    serializer = ArtistSerializer(artists, many=True)
    return Response(serializer.data)

  def post(self,request):
    # artists = Artist.objects.all()
    serializer = ArtistSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      data = {"message":"POST succes"}
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)


class ArtistDetail(APIView):
  def get_obj(self,request,pk):
    return get_object_or_404(Artist, id=pk) #! bir artist i aldık


  def get(self,request,pk):
    artist = self.get_obj(pk)
    serializer = ArtistSerializer(artist)
    return Response(serializer.data)


  def put(self,request,pk):
    artist = self.get_obj(pk)
    serializer = ArtistSerializer(instance=artist, data=request.data)
    if serializer.is_valid():
      serializer.save()
      message = {
      "message" : "Updated PUT"
      }
      return Response(message, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self,request,pk):
    artist = self.get_obj(pk)
    artist.delete()
    message = {
      "message" : "Artist DELETED"
    }
    return Response(message)


#!GENERİCAPIViews

#?GenericApiViews

#? Mixins


class ArtistGAV(mixins.ListModelMixin,mixins.CreateModelMixin,GenericAPIView):
  #GenericApiView
  quaryset = Artist.objects.all()
  serializer_class = ArtistSerializer

  #Listodeixins
  def get(self, request, *args, **kwargs):
    return self.list(request, *args, **kwargs)

#CreateModeMixins
  def post(self, request, *args, **kwargs):
    return self.create(request, *args, **kwargs)


class ArtistDetailGAV(mixins.RetrieveModelMixin,mixins.DestroyModelMixin,mixins.UpdateModelMixin,GenericAPIView):

  queryset=Artist.objects.all()
  serializer_class = ArtistSerializer
  #RetrieveModelMixin
  def get(self, request, *args, **kwargs):
    return self.retrieve(request, *args, **kwargs)

#DestroyModelMixin
  def delete(self, request, *args, **kwargs):
    return self.destroy(request, *args, **kwargs)

#UpdateModelMixin
  def put(self, request, *args, **kwargs):
    return self.update(request, *args, **kwargs)



#! Concrete Views

class ArtistCV(ListCreateAPIView):
  queryset=Artist.objects.all()
  serializer_class = ArtistSerializer


class ArtistDetailCV(RetrieveUpdateDestroyAPIView):
  queryset=Artist.objects.all()
  serializer_class = ArtistSerializer































