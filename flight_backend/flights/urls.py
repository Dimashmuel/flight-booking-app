from django.urls import path
from .views import (
    FlightListAPIView,
    BookingCreateAPIView,
    get_bookings,
    delete_booking
)

urlpatterns = [
    # Endpoint to list all available flights (GET)
    path('flights', FlightListAPIView.as_view(), name='flight-list'),

    # Endpoint to create a new booking (POST)
    path('book', BookingCreateAPIView.as_view(), name='booking-create'),

    # Endpoint to retrieve all bookings (GET)
    path('bookings', get_bookings),

    # Endpoint to delete a specific booking by ID (DELETE)
    path('bookings/<int:booking_id>', delete_booking),
]
