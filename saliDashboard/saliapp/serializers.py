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
    id_communication = CommunicationTypeSerializer()
    id_by_create = UserSerializer()

    class Meta:
        model = ControllerModule
        # id_communication = CommunicationTypeSerializer

        # id_communication = CommunicationTypeSerializer
        # id_by_create = UserSerializer
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
        fields = ('id',
                  'name',
                  'seding_time',
                  'status_sm',
                  'baterry_sm',
                  'localization_sm')


class SMperCMSerializer(serializers.HyperlinkedModelSerializer):
    id_sm = SensorModuleSerializer()
    id_cm = ControllerModuleSerializer()

    class Meta:
        model = SMPerCM
        fields = ('id_cm',
                  'id_sm',
                  )

class SensorSerializer(serializers.HyperlinkedModelSerializer):
    id_sm = SensorModuleSerializer()
    id_sensor_type = SensorTypeSerializer()
    class Meta:
        model = Sensor
        fields = ('id', 'id_sm', 'id_sensor_type')

class SensorPerSMSerializer(serializers.HyperlinkedModelSerializer):
    id_sensor_type = SensorTypeSerializer()
    class Meta:
        model = Sensor
        fields = ('id', 'id_sensor_type')


class ReadingSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Reading
        fields = ('id', 'value', 'date_time')


class AlarmsSettingsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AlarmsSettings
        fields = ('id', 'max', 'min', 'msgMax', 'msgMin')
