"""
from .models import Sensor
from .models import SensorMeasurements
from .models import Measure

from rest_framework import serializers


class SensorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sensor
        fields = ('id', 'name', 'coordination', 'temperature', 'salinity')


class SensorMeasurementsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SensorMeasurements
        fields = ('id', 'sensor', 'measure', 'day')
        #fields = '__all__'


class MeasureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Measure
        #fields = '__all__'
        fields = ('id', 'name', 'members')
"""