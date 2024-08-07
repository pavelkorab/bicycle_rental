from rest_framework.response import Response
from rest_framework.views import APIView
from.models import Rental
from.serializers import RentalSerializer

class RentalList(APIView):
    def get(self, request):
        rentals = Rental.objects.all()
        serializer = RentalSerializer(rentals, many=True)
        return Response(serializer.data)