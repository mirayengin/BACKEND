from django.contrib import admin
from django.urls import path, include
from .views import postclass,postclass1


urlpatterns = [
    path('post/', postclass),
    path('post1/', postclass1),

]