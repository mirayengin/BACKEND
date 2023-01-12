from django.urls import path,include
from .views import RegisterAPI,ProfileUpdateView

urlpatterns = [
    path('auth/', include('dj_rest_auth.urls')),
    path("register/", RegisterAPI.as_view()),
    path("profile/<init:pk>", ProfileUpdateView.as_view())
]
