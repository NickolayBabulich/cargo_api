from django.db import models
from location.models import Location


class Car(models.Model):
    number = models.CharField(max_length=5, unique=True)
    current_location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='car_location')
    load_capacity = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.number}'
