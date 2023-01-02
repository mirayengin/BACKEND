from rest_framework import serializers
from rest_framework.validators import UniqueValidator


from django.contrib.auth.models import User


class RegisterSerializer(serializers.ModelSerializer):
  #! her girilen email uniq oldu bu validator ile ve email sadece bir kez kullanıldı
  email =serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
  password = serializers.CharField(write_only=True)
  password2 = serializers.CharField(write_only=True, required =True) #? password check için passwordler de required default true
  first_name = serializers.CharField(required=True)

  class Meta:
    model = User
    # fields = "__all__"
    fields = ["id", "username", "email", "first_name", "last_name", "password","password2"]