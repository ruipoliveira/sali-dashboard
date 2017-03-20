
from .models import *

from rest_framework import serializers

class CommunicationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CommunicationType
        fields = ('id', 'name', 'path_or_number', 'image_path')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name')


class ControllerModuleSerializer(serializers.HyperlinkedModelSerializer):
    id_communication = CommunicationSerializer()
    id_by_create = UserSerializer()
    class Meta:
        model = ControllerModule
        fields = ('id',
                  'name',
                  'id_communication',
                  'id_by_create',
                  'baterry_cm',
                  'status_cm',
                  'date_create',
                  'memory',
                  'localization_cm')


class SensorModuleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SensorModule
        fields = ('id', 'name', 'seding_time', 'status_sm', 'baterry_sm', 'localization_sm')






class SensorSerializer(serializers.HyperlinkedModelSerializer):
    id_sm = SensorModuleSerializer()
    class Meta:
        model = Sensor
        fields = ('id', 'id_sm')