from django.shortcuts import render
from django.http  import HttpResponse

# Create your views here.
def Intersection(request):
  return HttpResponse("Hello intersection")


def IntersectionMembers(request):
  return HttpResponse("Hello intersection members")