from django.urls import path
from .views import FlightListAPIView, BookingCreateAPIView, get_bookings , delete_booking

urlpatterns = [
    path('flights', FlightListAPIView.as_view(), name='flight-list'),
    path('book', BookingCreateAPIView.as_view(), name='booking-create'),
    path('bookings', get_bookings),
    path('bookings/<int:booking_id>', delete_booking),
]
