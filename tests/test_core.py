from django.test import TestCase
from.models import Bike

class BikeTestCase(TestCase):
    def test_bike_creation(self):
        bike = Bike.objects.create(name='Test Bike', description='Test description')
        self.assertEqual(bike.name, 'Test Bike')