
from .models import *

from rest_framework import serializers



class ControllerModuleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ControllerModule
        fields = ('id', 'name')


class SensorModuleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SensorModule
        fields = ('id', 'name')


class SensorSerializer(serializers.HyperlinkedModelSerializer):
    id_sm = SensorModuleSerializer()
    class Meta:
        model = Sensor
        fields = ('id', 'id_sm')