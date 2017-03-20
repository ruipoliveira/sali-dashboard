from rest_framework import viewsets

from .serializers import *


class ControllerModuleViewSet(viewsets.ModelViewSet):
    queryset = ControllerModule.objects.all()
    serializer_class = ControllerModuleSerializer


class SensorModuleViewSet(viewsets.ModelViewSet):
    queryset = SensorModule.objects.all()
    serializer_class = SensorModuleSerializer


class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class CommunicationViewSet(viewsets.ModelViewSet):
    queryset = CommunicationType.objects.all()
    serializer_class = CommunicationSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
