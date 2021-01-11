from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from . import serializers
from etl import Pandas, Spark


class SalesViewSet(viewsets.GenericViewSet):
    serializer_class = serializers.SalesSerializer
    etl_engines = {
        'pandas': Pandas,
        'spark':  Spark,
    }
    csv_path = './data/dataset.csv'
    
    def get_queryset(self, etl_engine='pandas'):
        etl_engine = self.etl_engines[etl_engine]
        
        data_frame = etl_engine()
        
        return data_frame.read_csv(self.csv_path)
    
    @swagger_auto_schema(manual_parameters=[serializers.car_make],
                         operation_summary='Média do valor do carro por fabricante.')
    @action(detail=False)
    def avg_car_value_by_car_make(self, request, format=None):
        data_frame = self.get_queryset() \
            .avg('car_make', 'car_value')
        
        if request.query_params.get('car_make') is not None:
            data_frame.filter('car_make', request.query_params.get('car_make'))
        
        return Response(data_frame)
    
    @swagger_auto_schema(manual_parameters=[serializers.city],
                         operation_summary='Média do valor do carro por cidade.')
    @action(detail=False)
    def avg_car_value_by_city(self, request, format=None):
        data_frame = self.get_queryset(etl_engine='spark') \
            .avg('city', 'car_value')
        
        if request.query_params.get('city') is not None:
            data_frame.filter('city', request.query_params.get('city'))
        
        return Response(data_frame)
