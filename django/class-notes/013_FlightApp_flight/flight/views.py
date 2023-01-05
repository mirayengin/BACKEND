from django.shortcuts import render
from rest_framework import viewsets
from .serializers import FlightSerializer
from .models import Flight,Passenger,Reservation
# Create your views her

class FlightView(viewsets.ModelViewSet):
  queryset = Flight.objects.all()
  serializer_class = FlightSerializer