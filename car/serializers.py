from rest_framework import serializers
from car.models import Car
from location.serializers import LocationSerializer


class CarSerializer(serializers.ModelSerializer):
    current_location = LocationSerializer()

    class Meta:
        model = Car
        fields = ['id', 'number', 'current_location', 'load_capacity']
