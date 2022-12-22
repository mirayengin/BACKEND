from django.urls import path
from .views import Intersection
from .views import IntersectionMembers

urlpatterns = [
    path('one/', Intersection),
    path('two/', IntersectionMembers),

]