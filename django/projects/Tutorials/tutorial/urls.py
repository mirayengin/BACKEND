
from django.urls import path,include
from rest_framework import routers
from .views  import Tutorials




router = routers.DefaultRouter()
router.register('tutorials',  Tutorials)

urlpatterns = [

    path('', include(router.urls)),
]