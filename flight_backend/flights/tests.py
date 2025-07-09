from django.test import TestCase, Client
from django.urls import reverse

class FlightsEndpointTest(TestCase):
    """
    Test case for the flights API endpoint.
    """

    def setUp(self):
        """
        Set up a test client before each test.
        """
        self.client = Client()

    def test_flights_endpoint_returns_200(self):
        """
        Ensure that a GET request to /api/flights/ returns HTTP 200.
        """
        response = self.client.get('/api/flights/')
        self.assertEqual(response.status_code, 200)
