import os
import django
import random
from datetime import date, timedelta, time

# Set up Django environment (only needed when running this script outside manage.py)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "flight_project.settings")
django.setup()

from flights.models import Flight

# List of real IATA airport codes
airports = [
    "JFK", "LHR", "CDG", "HND", "DXB", "YYZ", "FCO", "MAD",
    "BER", "IST", "SYD", "BKK", "AMS", "LAX", "ORD", "TLV"
]

# List of real airline names
airlines = [
    "Delta Airlines", "British Airways", "Air France", "Emirates", "Turkish Airlines",
    "Lufthansa", "American Airlines", "Qatar Airways", "Air Canada", "KLM", "EL AL"
]

def create_random_flight():
    """
    Generates a single Flight instance with randomized origin, destination,
    date, time, and airline. Ensures origin ≠ destination.
    """
    origin = random.choice(airports)
    destination = random.choice([code for code in airports if code != origin])
    departure_date = date.today() + timedelta(days=random.randint(1, 90))
    departure_time = time(hour=random.randint(0, 23), minute=random.choice([0, 15, 30, 45]))
    airline = random.choice(airlines)
    return Flight(
        origin=origin,
        destination=destination,
        departure_date=departure_date,
        departure_time=departure_time,
        airline=airline
    )

# Create 1000 random Flight instances
flights = [create_random_flight() for _ in range(1000)]

# Bulk insert all flights into the database
Flight.objects.bulk_create(flights)

print("✅ Successfully created 1000 flights.")
