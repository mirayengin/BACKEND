from django.shortcuts import render
from django.contrib.auth.models import User
from .serializer import RegisterSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.authtoken.models import Token

from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer



    def create(self, request, *args, **kwargs): #! override
        response = super().create(request, *args, **kwargs)
        print(response.data)  #!Burdakiler serializer daki fieldsler dir

        token = Token.objects.create(user_id = response.data["id"])

        #! Bu token Token adıyla import ettiğimiz class dan alıyoruz
        response.data["token"] = token.key
        print(response.data)  #!Yukarıdakine ek olarak token var

        return response


@api_view(['POST'])
def logout(request):
    request.user.auth_token.delete()
    return Response({"message": 'User Logout: Token Deleted'})