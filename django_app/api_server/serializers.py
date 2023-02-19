from rest_framework import serializers
from .models import *

class Livedataserializer(serializers.ModelSerializer):
    class Meta:
        model = live_data
        fields ='__all__'