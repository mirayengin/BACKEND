from rest_framework import serializers
from .models import Student


# #? Banckend de bizim yerimize işleri yapacak bir serializer yazıyoruz
# #! Burada önceden model de yazdığımız field ları data aktarımı için buraya yazıyoruz
# #? serializers.Serializer bu serializer için ilkel bir metoddur
# class StudentSerializer(serializers.Serializer):
#   first_name = serializers.ChardFiled(max_lenght=50)
#   last_name = serializers.ChardFiled(max_lenght=50)
#   number = serializers.IntegerFiled()
#   age = serializers.IntegerFiled()



# #! Filed ları elle yazdığımız zaman burada extra olarak create ve update metodlarını yazmamız lazım
#   def create(self, validated_data):
#     return Student.objects.create(**validated_data)

#   def update(self, instance, validated_data):
#     instance.first_name = validated_data.get('first_name', instance.first_name)
#     instance.last_name = validated_data.get('last_name', instance.last_name)
#     instance.number = validated_data.get('number', instance.number)
#     instance.age = validated_data.get('age', instance.age)
#     instance.save()
#     return instance

#! Bu metod cok kullandığımız metoddur. bu bize fieldları tet tek yazmamamızı ve create ve update metodlarını yazmamamıza gerek olmamasını sağlar
class StudentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Student
    # fields = "__all__"
    #! Eğer ki biz database den sadece istediklerimizi almak istiyorsak bu şekilde yazıyoruz
    fields = ["id","first_name", "last_name","age"]
    #! number dışındakileri getirir
    exclude = ["number"]


#? Yukarıda bulunan ilkel metodun tüm işini bu yapabiliyor