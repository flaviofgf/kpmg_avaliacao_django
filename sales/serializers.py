from drf_yasg import openapi
from rest_framework import serializers

car_make = openapi.Parameter('car_make', openapi.IN_QUERY, description='Fabricante', type=openapi.TYPE_STRING,
                             required=False)
city = openapi.Parameter('city', openapi.IN_QUERY, description='Cidade', type=openapi.TYPE_STRING, required=False)


class SalesSerializer(serializers.Serializer):
    city = serializers.CharField(required=False)
    car_make = serializers.CharField(required=False)
    car_value = serializers.IntegerField(required=True, label='avg(car_value)')
    
    def update(self, instance, validated_data):
        pass
    
    def create(self, validated_data):
        pass
