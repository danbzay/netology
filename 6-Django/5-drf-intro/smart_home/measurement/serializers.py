from rest_framework import serializers

from .models import Measurement, Sensor

# TODO: опишите необходимые сериализаторы

class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['sensor', 'temperature', 'measurement_datetime', 'image']

class SensorSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(read_only=True, many=True)
    class Meta:
        model = Sensor
        fields = ['name', 'description', 'measurements']

