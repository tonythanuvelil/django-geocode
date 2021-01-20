from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Order
from .services import get_location_detail


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('house_name', 'latitude', 'longitude',
                  'address', 'country', 'postcode',)


class OrderView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk=None):
        if pk is not None:
            order = Order.objects.get(pk=pk).filter(user=request.user)
        else:
            order = Order.objects.all().filter(user=request.user)
        serializer = OrderSerializer(order, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        location_details = get_location_detail(
            request.data['latitude'], request.data['longitude'])
        data['postcode'] = int(location_details['postalCode'])
        data['country'] = location_details['adminArea1']
        data['address'] = location_details['street']
        serializer = OrderSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response(status=status.HTTP_201_CREATED)

    def patch(self, request, pk, format=None):
        order = Order.objects.get(pk=pk)
        serializer = OrderSerializer(order, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        order = Order.objects.get(pk=pk)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
