# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from rest_framework import generics, viewsets

from .serializers import MeasurementSerializer, SensorSerializer
from .models import Measurement, Sensor

class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class MeasurementViewSet(viewsets.ModelViewSet):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

"""
class SensorList(generic.ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class CreateSensor(generic.CreateAPIView):
    serializer_class = SensorSerializer

class RetieveUpdateSensor(generic.RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class DestroySensor(generic.DestroyAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
"""
