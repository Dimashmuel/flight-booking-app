from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Flight
from .serializers import FlightSerializer

class FlightListAPIView(APIView):
    def get(self, request):
        flights = Flight.objects.all()
        serializer = FlightSerializer(flights, many=True)
        return Response(serializer.data)

from rest_framework import status
from rest_framework.response import Response
from .serializers import BookingSerializer

class BookingCreateAPIView(APIView):
    def post(self, request):
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Booking created successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from django.http import JsonResponse
from .models import Booking

def get_bookings(request):
    bookings = Booking.objects.select_related('flight').all()
    data = [
        {
            'name': b.passenger_name,
            'email': b.passenger_email,
            'origin': b.flight.origin,
            'destination': b.flight.destination,
            'date': b.flight.departure_date,
            'time': b.flight.departure_time,
            'airline': b.flight.airline,
            'flight_id': b.flight.id,
            'booking_id': b.id
        }
        for b in bookings
    ]
    return JsonResponse(data, safe=False)


from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponseNotAllowed
from .models import Booking

@csrf_exempt
def delete_booking(request, booking_id):
    if request.method == 'DELETE':
        try:
            booking = Booking.objects.get(id=booking_id)
            booking.delete()
            return JsonResponse({'message': 'Booking deleted.'})
        except Booking.DoesNotExist:
            return JsonResponse({'error': 'Booking not found.'}, status=404)
    return HttpResponseNotAllowed(['DELETE'])
