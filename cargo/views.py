from rest_framework import generics, status
from rest_framework.response import Response
from geopy.distance import distance
from location.models import Location
from cargo.models import Cargo
from cargo.serializers import CargoSerializer
from car.models import Car
from car.serializers import CarSerializer


class CargoCreateAPIView(generics.CreateAPIView):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer

    def create(self, request, *args, **kwargs):
        zip_pickup = request.data.get('zip_pickup')
        zip_delivery = request.data.get('zip_delivery')
        location_pickup = Location.objects.get(zip_code=zip_pickup)
        location_delivery = Location.objects.get(zip_code=zip_delivery)
        weight = request.data.get('weight')
        description = request.data.get('description')
        cargo = Cargo.objects.create(
            location_pickup=location_pickup,
            location_delivery=location_delivery,
            weight=weight,
            description=description
        )
        cargo.save()
        serializer = self.get_serializer(cargo)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CargoListAPIView(generics.ListAPIView):
    serializer_class = CargoSerializer

    def get_queryset(self):
        cargos = Cargo.objects.all()
        return cargos

    def list(self, request, *args, **kwargs):
        cargos = self.get_queryset()
        serializer = self.get_serializer(cargos, many=True)
        cargoes_data = serializer.data
        for cargo in cargoes_data:
            cars = Car.objects.all()
            nearest_cars = []
            for car in cars:
                car_location = (car.current_location.latitude, car.current_location.longitude)
                location_pickup = (cargo['location_pickup']['latitude'], cargo['location_pickup']['longitude'])
                distance_in_miles = distance(car_location, location_pickup).miles
                if distance_in_miles <= 450:
                    nearest_cars.append(
                        {
                            'id': car.pk,
                            'number': car.number,
                            'current_location': {
                                'city': car.current_location.city,
                                'state': car.current_location.state,
                                'zip_code': car.current_location.zip_code,
                                'latitude': car.current_location.latitude,
                                'longitude': car.current_location.longitude
                            },
                            'load_capacity': car.load_capacity,
                            'distance': f'{int(distance_in_miles)} miles'
                        }
                    )
            cargo['nearest_cars'] = len(nearest_cars)
        return Response(serializer.data)


class CargoRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        location_pickup = (instance.location_pickup.latitude, instance.location_pickup.longitude)
        cars = Car.objects.all()
        cars_with_distance = []
        for car in cars:
            car_location = (car.current_location.latitude, car.current_location.longitude)
            car_distance = distance(location_pickup, car_location).miles
            car_data = CarSerializer(car).data
            car_data['distance'] = f'{int(car_distance)} miles'
            cars_with_distance.append(car_data)
        cars_with_distance.sort(key=lambda x: x['distance'])
        instance.cars = cars_with_distance
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class CargoUpdateAPIView(generics.UpdateAPIView):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        weight = request.data.get('weight')
        description = request.data.get('description')
        if weight is not None:
            instance.weight = weight
        if description is not None:
            instance.description = description
        instance.save()
        serializer = self.get_serializer(instance)

        return Response(serializer.data)


class CargoDeleteAPIView(generics.DestroyAPIView):
    queryset = Cargo.objects.all()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'message': 'Груз успешно удален', 'status': status.HTTP_204_NO_CONTENT})
