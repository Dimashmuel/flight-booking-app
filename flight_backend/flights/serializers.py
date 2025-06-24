from rest_framework import serializers
from .models import Flight , Booking

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['flight', 'passenger_name', 'passenger_email']
