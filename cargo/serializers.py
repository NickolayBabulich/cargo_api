from rest_framework import serializers
from cargo.models import Cargo
from location.serializers import LocationSerializer


class CargoSerializer(serializers.ModelSerializer):
    location_pickup = LocationSerializer()
    location_delivery = LocationSerializer()
    cars = serializers.ListField(child=serializers.DictField(), read_only=True)

    class Meta:
        model = Cargo
        fields = ['id', 'location_pickup', 'location_delivery', 'weight', 'description', 'cars']
