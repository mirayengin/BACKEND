from rest_framework import serializers
from django.contrib.auth.models import User


from rest_framework.validators import UniqueValidator

# from django.conf import settings  #? Buda user a işaret ediyor


class RegisterSerializer(serializers.ModelSerializer):
  #? Burda login olurken kullandığımız fielslerin özelliklerini değiştirdik (örn=gerekli,boş bırakılabilir gibi)
  #! valisator ile database e user ların uniq olarak kaydını sağladık
  email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
  password = serializers.CharField(write_only=True) #! Bu fields ı sadece post işleminde kullan(write_only)
  # password = serializers.CharField(reade_only=True) #! Bu fields ı sadece get işleminde kullan(read_only)
  password2 = serializers.CharField(write_only=True, required=True)

  class Meta:
    #? default olan user modelinin özelliklerini inharent ettik
    model = User
    fields = (
      "id",
      "username",
      "email",
      "first_name",
      "last_name",

      #! write only olduğu için passwordleri sadece create zamanı görüyoruz
      "password",
      "password2"
    )
