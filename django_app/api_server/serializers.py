from rest_framework import serializers
from .models import *

class Livedataserializer(serializers.ModelSerializer):
    class Meta:
        model = live_data
        fields ='__all__'
    
class Studentdetailsserializer(serializers.ModelSerializer):
    class Meta:
        model = Student_details
        fields ='__all__'

class Attendance_serializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance_details
        fields ='__all__'