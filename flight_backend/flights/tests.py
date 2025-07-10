from django.test import TestCase
from .models import Flight, Booking
from rest_framework.test import APIClient
from rest_framework import status

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


class FlightAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.flight = Flight.objects.create(
            origin="NYC",
            destination="LON",
            departure_date="2025-08-10",
            departure_time="16:00:00",
            airline="British Airways"
        )

    def test_get_flights(self):
        response = self.client.get('/api/flights')  
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['origin'], "NYC")

class BookingAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.flight = Flight.objects.create(
            origin="BOS",
            destination="PAR",
            departure_date="2025-08-12",
            departure_time="09:00:00",
            airline="Air France"
        )
        self.booking_data = {
            'flight': self.flight.id,
            'passenger_name': "Alice",
            'passenger_email': "alice@example.com"
        }

    def test_create_booking(self):
        response = self.client.post('/api/book', self.booking_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete_booking(self):
        booking = Booking.objects.create(
            flight=self.flight,
            passenger_name="Alice",
            passenger_email="alice@example.com"
        )
        response = self.client.delete(f'/api/bookings/{booking.id}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
