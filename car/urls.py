from django.urls import path
from car.views import CarUpdateAPIView

urlpatterns = [
    path('car/update/<int:pk>/', CarUpdateAPIView.as_view(), name='update-car'),
]
