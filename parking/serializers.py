from rest_framework.serializers import ModelSerializer
from rest_framework import  serializers
from .models import Car


class CarSerializer(ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'
        depth = 1
