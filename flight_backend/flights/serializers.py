from rest_framework import serializers
from .models import Flight, Booking

class FlightSerializer(serializers.ModelSerializer):
    """
    Serializer for the Flight model.
    Serializes all fields of the Flight instance.
    """
    class Meta:
        model = Flight
        fields = '__all__'  # Include all fields from the Flight model


class BookingSerializer(serializers.ModelSerializer):
    """
    Serializer for the Booking model.
    Only includes selected fields (excludes 'booked_at' for simplicity).
    """
    class Meta:
        model = Booking
        fields = ['flight', 'passenger_name', 'passenger_email']
