from rest_framework import serializers
from .models import Weather,Testing

class TaskSerializer(serializers.ModelSerializer):
    # class Meta:
    #     model = Weather
    #     fields ='__all__'
    
    class Meta:
        model = Testing
        fields ='__all__'