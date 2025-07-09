from django.test import TestCase
from flights.models import Flight
from datetime import datetime

class FlightModelTest(TestCase):
    def test_flight_creation(self):
        flight = Flight.objects.create(
            origin='CDG',
            destination='TLV',
            airline='Air France',
            date=datetime(2025, 9, 1),
            time=datetime(2025, 9, 1, 15, 30).time()
        )
        self.assertEqual(Flight.objects.count(), 1)
        self.assertEqual(flight.destination, 'TLV')