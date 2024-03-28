from django.urls import path
from cargo.views import (
    CargoCreateAPIView,
    CargoListAPIView,
    CargoRetrieveAPIView,
    CargoUpdateAPIView,
    CargoDeleteAPIView
)

urlpatterns = [
    path('cargo/create/', CargoCreateAPIView.as_view(), name='create-cargo'),
    path('cargoes/', CargoListAPIView.as_view(), name='list-cargoes'),
    path('cargo/<int:pk>/', CargoRetrieveAPIView.as_view(), name='view-cargo'),
    path('cargo/update/<int:pk>/', CargoUpdateAPIView.as_view(), name='update-cargo'),
    path('cargo/delete/<int:pk>/', CargoDeleteAPIView.as_view(), name='delete-cargo'),
]
