from celery import shared_task
from car.models import Car
from location.models import Location


@shared_task
def update_car_locations():
    cars = Car.objects.all()
    for car in cars:
        location = Location.objects.order_by('?').first()
        car.current_location = location
        car.save()
