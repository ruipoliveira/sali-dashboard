from .models import *

from rest_framework import serializers


class CommunicationTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CommunicationType
        fields = ('id', 'name', 'path_or_number', 'image_path')


class SensorTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SensorType
        fields = ('id', 'name', 'scale_value', 'image_path', 'color')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'last_login', 'date_joined')


class ControllerModuleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ControllerModule
        id_communication = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)

        #id_communication = CommunicationTypeSerializer
        #id_by_create = UserSerializer
        fields = ('id',
                  'name',
                  'id_communication',
                  #'id_by_create',
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
