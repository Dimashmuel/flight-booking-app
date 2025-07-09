from django.test import TestCase
from .models import Flight, Booking

class FlightModelTest(TestCase):
    def test_flight_creation(self):
        flight = Flight.objects.create(
            origin="CDG",
            destination="TLV",
            departure_date="2025-08-02",
            departure_time="12:30:00",
            airline="KLM"
        )
        self.assertEqual(flight.origin, "CDG")
        self.assertEqual(flight.destination, "TLV")
        self.assertEqual(flight.airline, "KLM")

class BookingModelTest(TestCase):
    def test_booking_creation(self):
        flight = Flight.objects.create(
            origin="CDG",
            destination="AMS",
            departure_date="2025-08-05",
            departure_time="10:00:00",
            airline="Air France"
        )
        booking = Booking.objects.create(
            flight=flight,
            passenger_name="John Doe",
            passenger_email="john@example.com"
        )
        self.assertEqual(booking.passenger_name, "John Doe")
        self.assertEqual(booking.flight.destination, "AMS")
