from django.test import TestCase
from django.urls import reverse
from rest_framework import status

class FlightsEndpointTest(TestCase):
    def test_flights_endpoint_returns_200(self):
        response = self.client.get('/flights/')
        self.assertEqual(response.status_code, 200)