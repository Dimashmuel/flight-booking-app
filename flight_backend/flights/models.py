from django.db import models

class Flight(models.Model):
    # Origin city or airport
    origin = models.CharField(max_length=100)

    # Destination city or airport
    destination = models.CharField(max_length=100)

    # Date of departure
    departure_date = models.DateField()

    # Time of departure
    departure_time = models.TimeField()

    # Airline operating the flight
    airline = models.CharField(max_length=100)

    def __str__(self):
        # String representation used in admin and debug output
        return f"{self.airline}: {self.origin} to {self.destination} on {self.departure_date}"


class Booking(models.Model):
    # Reference to the flight being booked
    flight = models.ForeignKey(
        Flight,
        on_delete=models.CASCADE,
        related_name='bookings'
    )

    # Name of the passenger making the booking
    passenger_name = models.CharField(max_length=100)

    # Email of the passenger
    passenger_email = models.EmailField()

    # Timestamp when the booking was created
    booked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # String representation used in admin and debug output
        return f"{self.passenger_name} ({self.passenger_email}) - {self.flight}"
