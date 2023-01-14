from rest_framework import serializers
from .models import Department, Personnel
from django.utils.timezone import now



class DepartmentSerializer(serializers.ModelSerializer):
    personel_count = serializers.SerializerMethodField()
    class Meta:
        model = Department
        fields = ('id',"personel_count", "name")

    def get_personel_count(self,obj):
        return obj.personals.count()


class PersonnelSerializer(serializers.ModelSerializer):
  days_since_joined = serializers.SerializerMethodField()
  create_user_id  = serializers.IntegerField(required=False)
  create_user = serializers.StringRelatedField()



  class Meta:
      model = Personnel
      fields = ("first_name", "last_name", "title", "gender")


  def create(self,validated_data):
      validated_data["create_user_id"] = self.context["request"].user.id
      return super().create(validated_data)
      
  def get_days_since_joined(self,obj):
    return (now() - obj.start_date).days



class DepartmentPersonnelSerializer(serializers.ModelSerializer):
    
    personnel_count = serializers.SerializerMethodField()
    personals = PersonnelSerializer(many=True, read_only=True)
    
    class Meta:
        model = Department
        fields = ("id", "name", "personnel_count", "personals")
        
    def get_personnel_count(self, obj):
        return obj.personals.count()






    