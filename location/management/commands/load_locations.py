import csv
from django.core.management import BaseCommand
from location.models import Location


class Command(BaseCommand):
    def handle(self, *args, **options):
        if not Location.objects.count():
            with open('uszips.csv', 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    city = row['city']
                    state = row['state_name']
                    zip_code = row['zip']
                    latitude = row['lat']
                    longitude = row['lng']

                    Location.objects.create(city=city,
                                            state=state,
                                            zip_code=zip_code,
                                            latitude=latitude,
                                            longitude=longitude)
            return f'Данные локаций успешно инициализированы!'
        return f'Данные локаций уже инициализированы!'
