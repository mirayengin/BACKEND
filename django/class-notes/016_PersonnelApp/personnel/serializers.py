from rest_framework import serializers
from .models import Department, Personnel



class DepartmentSerializer(serializers.ModelSerializer):
    personel_count = serializers.SerializerMethodField()
    class Meta:
        model = Department
        fields = ('id',"personel_count", "name")

    def get_personel_count(self,obj):
        return obj.personals.count()


class PersonnelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personnel
        fields = ("first_name", "last_name", "title", "gender")



    