from django.db import models
from location.models import Location


class Cargo(models.Model):
    location_pickup = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='pickup_cargo')
    location_delivery = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='delivery_cargo')
    weight = models.PositiveIntegerField()
    description = models.TextField()

    def __str__(self):
        return f'{self.id}'
