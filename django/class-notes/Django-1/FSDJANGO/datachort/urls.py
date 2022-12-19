
from django.urls import path,include
from .views import homedata

urlpatterns = [

    path('', homedata)
]