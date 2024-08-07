from rest_framework.response import Response
from rest_framework.views import APIView
from.models import Bike
from.serializers import BikeSerializer

class BikeList(APIView):
    def get(self, request):
        bikes = Bike.objects.all()
        serializer = BikeSerializer(bikes, many=True)
        return Response(serializer.data)