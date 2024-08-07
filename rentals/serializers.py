from rest_framework import serializers
from.models import Rental

class RentalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rental
        fields = ['id', 'bike', 'user', 'tart_time', 'end_time', 'cost']