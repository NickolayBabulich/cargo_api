from rest_framework import generics, status
from rest_framework.response import Response
from car.models import Car
from car.serializers import CarSerializer
from location.models import Location


class CarUpdateAPIView(generics.UpdateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        zip_code = request.data.get('zip_code')
        if zip_code:
            try:
                location = Location.objects.get(zip_code=zip_code)
                instance.current_location = location
            except Location.DoesNotExist:
                return Response({'error': 'Location not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
