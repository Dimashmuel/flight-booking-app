from django.db import models

class Flight(models.Model):
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    departure_date = models.DateField()
    departure_time = models.TimeField()
    airline = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.airline}: {self.origin} to {self.destination} on {self.departure_date}"

class Booking(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name='bookings')
    passenger_name = models.CharField(max_length=100)
    passenger_email = models.EmailField()
    booked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.passenger_name} ({self.passenger_email}) - {self.flight}"
