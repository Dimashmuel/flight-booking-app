from django.test import TestCase, Client
from django.urls import reverse

class FlightsEndpointTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_flights_endpoint_returns_200(self):
        response = self.client.get('/api/flights/')
        self.assertEqual(response.status_code, 200)