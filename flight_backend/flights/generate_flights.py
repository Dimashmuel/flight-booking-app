import os
import django
import random
from datetime import date, timedelta, time

# הגדרת הסביבה (רק אם מריצים מחוץ ל־manage.py)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "flight_project.settings")
django.setup()

from flights.models import Flight

# רשימת נמלי תעופה אמיתיים (קוד IATA)
airports = [
    "JFK", "LHR", "CDG", "HND", "DXB", "YYZ", "FCO", "MAD",
    "BER", "IST", "SYD", "BKK", "AMS", "LAX", "ORD", "TLV"
]

# חברות תעופה אמיתיות
airlines = [
    "Delta Airlines", "British Airways", "Air France", "Emirates", "Turkish Airlines",
    "Lufthansa", "American Airlines", "Qatar Airways", "Air Canada", "KLM", "EL AL"
]

def create_random_flight():
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

# יצירת 500 טיסות
flights = [create_random_flight() for _ in range(1000)]
Flight.objects.bulk_create(flights)

print("✅ Successfully created 500 flights.")
