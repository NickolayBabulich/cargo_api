import random
import string
from django.core.management import BaseCommand
from car.models import Car
from location.models import Location


class Command(BaseCommand):
    def handle(self, *args, **options):
        if not Car.objects.count():
            for i in range(20):
                number = str(random.randint(1000, 9999)) + random.choice(string.ascii_uppercase)
                current_location = Location.objects.order_by('?').first()
                load_capacity = random.randint(1, 1000)
                Car.objects.create(number=number,
                                   current_location=current_location,
                                   load_capacity=load_capacity)
            return f'Данные автомобилей успешно инициализированы'
        print(Location.objects.get(zip_code='02779'))
        return f'Данные автомобилей уже инициализированы'
