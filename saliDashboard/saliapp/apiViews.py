from datetime import datetime

from django.core.exceptions import ObjectDoesNotExist
from rest_framework import viewsets
from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.views import APIView

from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class ControllerModuleViewSet(APIView):

    def get(self, request, format=None):
        users = ControllerModule.objects.all()
        serializer = ControllerModuleSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ControllerModuleSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SensorModuleViewSet(viewsets.ModelViewSet):
    queryset = SensorModule.objects.all()
    serializer_class = SensorModuleSerializer


class CommunicationViewSet(viewsets.ModelViewSet):
    queryset = CommunicationType.objects.all()
    serializer_class = CommunicationTypeSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


#########################################################
# Communication Type
#########################################################

class CommunicationTypeList(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        snippets = CommunicationType.objects.all()
        serializer = CommunicationTypeSerializer(snippets, many=True, context={'request': request,
                                                                               'user': unicode(request.user),
                                                                               'auth': unicode(request.auth), })
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CommunicationTypeSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommunicationType_param(APIView):
    def get_object(self, pk_or_name):
        if pk_or_name.isdigit():
            try:
                return CommunicationType.objects.get(pk=pk_or_name)
            except CommunicationType.DoesNotExist:
                raise Http404
        else:
            try:
                return CommunicationType.objects.get(name__iexact=pk_or_name)
            except CommunicationType.DoesNotExist:
                raise Http404

    def get(self, request, pk_or_name, format=None):
        comm = self.get_object(pk_or_name)
        serializer = CommunicationTypeSerializer(comm, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk_or_name, format=None):
        comm = self.get_object(pk_or_name)
        serializer = CommunicationTypeSerializer(comm, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk_or_name, format=None):
        snippet = self.get_object(pk_or_name)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#########################################################
# Sensor Type
#########################################################

class SensorTypeList(APIView):
    def get(self, request, format=None):
        sensor = SensorType.objects.all()
        serializer = SensorTypeSerializer(sensor, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SensorTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SensorType_param(APIView):
    def get_object(self, pk_or_name):
        if pk_or_name.isdigit():
            try:
                return CommunicationType.objects.get(pk=pk_or_name)
            except CommunicationType.DoesNotExist:
                raise Http404
        else:
            try:
                return CommunicationType.objects.get(name__iexact=pk_or_name)
            except CommunicationType.DoesNotExist:
                raise Http404

    def get(self, request, pk_or_name, format=None):
        sensor = self.get_object(pk_or_name)
        serializer = CommunicationTypeSerializer(sensor)
        return Response(serializer.data)

    def put(self, request, pk_or_name, format=None):
        sensor = self.get_object(pk_or_name)
        serializer = CommunicationTypeSerializer(sensor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk_or_name, format=None):
        sensor = self.get_object(pk_or_name)
        sensor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#########################################################
# Users
#########################################################

class UserList(APIView):
    def get(self, request, format=None):
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class User_param(APIView):
    def get_object(self, pk_or_username):
        if pk_or_username.isdigit():
            try:
                return User.objects.get(pk=pk_or_username)
            except User.DoesNotExist:
                raise Http404
        else:
            try:
                return User.objects.get(username__iexact=pk_or_username)
            except User.DoesNotExist:
                raise Http404

    def get(self, request, pk_or_username, format=None):
        user = self.get_object(pk_or_username)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk_or_username, format=None):
        user = self.get_object(pk_or_username)
        serializer = CommunicationTypeSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk_or_username, format=None):
        user = self.get_object(pk_or_username)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#########################################################
# Controller module
#########################################################

class ControllerModuleList(APIView):
    def get(self, request, format=None):
        cm = ControllerModule.objects.all()
        serializer = ControllerModuleSerializer(cm, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ControllerModuleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ControllerModule_param(APIView):
    def get_object(self, pk_or_name):
        if pk_or_name.isdigit():
            try:
                return ControllerModule.objects.get(pk=pk_or_name)
            except ControllerModule.DoesNotExist:
                raise Http404
        else:
            try:
                return ControllerModule.objects.get(name__iexact=pk_or_name)
            except ControllerModule.DoesNotExist:
                raise Http404

    def get(self, request, pk_or_name, format=None):
        cm = self.get_object(pk_or_name)
        serializer = ControllerModuleSerializer(cm)
        return Response(serializer.data)

    def put(self, request, pk_or_name, format=None):
        cm = self.get_object(pk_or_name)
        serializer = ControllerModuleSerializer(cm, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk_or_name, format=None):
        cm = self.get_object(pk_or_name)
        cm.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#########################################################
# CM per user
#########################################################

class CMperUser_param(ListCreateAPIView):
    queryset = CMPerUsers.objects.all()
    serializer_class = CMperUserSerializer

    def list(self, request, pk_or_username):
        # Note the use of `get_queryset()` instead of `self.queryset`

        try:
            if pk_or_username.isdigit():
                queryset = CMPerUsers.objects.filter(id_user=User.objects.get(id=pk_or_username))

            else:
                queryset = CMPerUsers.objects.filter(id_user=User.objects.get(username=pk_or_username))
        except ObjectDoesNotExist:
            queryset = None

        serializer = CMperUserSerializer(queryset, many=True)

        return Response(serializer.data)


#########################################################
# Sensor module
##################r#######################################

class SensorModuleList(APIView):
    def get(self, request, format=None):
        sm = SensorModule.objects.all()
        serializer = SensorModuleSerializer(sm, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SensorModuleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SensorModule_param(APIView):
    def get_object(self, pk_or_name):

        if pk_or_name.isdigit():
            try:
                return SensorModule.objects.get(pk=pk_or_name)
            except ControllerModule.DoesNotExist:
                raise Http404
        else:
            try:
                return SensorModule.objects.get(name__iexact=pk_or_name)
            except ControllerModule.DoesNotExist:
                raise Http404

    def get(self, request, pk_or_name, format=None):
        sm = self.get_object(pk_or_name)
        serializer = SensorModuleSerializer(sm)
        return Response(serializer.data)

    def put(self, request, pk_or_name, format=None):
        sm = self.get_object(pk_or_name)
        serializer = SensorModuleSerializer(sm, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk_or_name, format=None):
        sm = self.get_object(pk_or_name)
        sm.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#########################################################
# Sensor module per Controller module
#########################################################

class SMperCMList(APIView):
    def get(self, request, format=None):
        sm = SMPerCM.objects.all()
        serializer = SMperCMSerializer(sm, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SensorModuleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SMperCM_param(ListCreateAPIView):
    queryset = SMPerCM.objects.all()
    serializer_class = SMperCMSerializer

    def list(self, request, pk_or_name_cm):
        # Note the use of `get_queryset()` instead of `self.queryset`
        if pk_or_name_cm.isdigit():
            queryset = SMPerCM.objects.filter(id_cm=pk_or_name_cm)
        else:
            queryset = SMPerCM.objects.filter(id_cm=ControllerModule.objects.get(name__iexact=pk_or_name_cm))
        serializer = SMperCMSerializer(queryset, many=True)
        return Response(serializer.data)


#########################################################
# Sensor
#########################################################

class SensorList(APIView):
    def get(self, request, format=None):
        sensor = Sensor.objects.all()
        serializer = SensorSerializer(sensor, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SensorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Sensor_param(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def list(self, request, pk_or_sensor_type):
        # Note the use of `get_queryset()` instead of `self.queryset`

        if pk_or_sensor_type.isdigit():
            queryset = Sensor.objects.filter(id=pk_or_sensor_type)
        else:
            queryset = Sensor.objects.filter(id_sensor_type=SensorType.objects.get(name__iexact=pk_or_sensor_type))
        serializer = SensorSerializer(queryset, many=True)
        return Response(serializer.data)


#########################################################
# Sensor per sensor module
#########################################################

class SensorperSM_param(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorPerSMSerializer

    def list(self, request, id_sm_or_name_sm):
        # Note the use of `get_queryset()` instead of `self.queryset`

        if id_sm_or_name_sm.isdigit():
            queryset = Sensor.objects.filter(id_sm=id_sm_or_name_sm)
        else:
            queryset = Sensor.objects.filter(id_sm=SensorModule.objects.get(name__iexact=id_sm_or_name_sm))
        serializer = SensorPerSMSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, id_sm_or_name_sm, format=None):

        if id_sm_or_name_sm.isdigit():
            queryset = Sensor.objects.filter(id_sm=id_sm_or_name_sm)
        else:
            queryset = Sensor.objects.filter(id_sm=SensorType.objects.get(name__iexact=id_sm_or_name_sm))

        serializer = SensorSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#########################################################
# Reading per sensor
#########################################################

class Reading_param(ListCreateAPIView):
    queryset = Reading.objects.all()
    serializer_class = SensorPerSMSerializer

    def list(self, request, id_sensor, date_start, date_end):
        # Note the use of `get_queryset()` instead of `self.queryset`

        queryset = Reading.objects.filter(id_sensor=Sensor.objects
                                          .get(pk=id_sensor), date_time__range=[date_start + ' 00:00:00',
                                                                                date_end + ' 23:59:59'])

        serializer = ReadingSerializer(queryset, many=True)
        return Response(serializer.data)


class Reading_param_all(ListCreateAPIView):
    queryset = Reading.objects.all()
    serializer_class = ReadingSerializer

    def list(self, request, id_sensor):
        # Note the use of `get_queryset()` instead of `self.queryset`

        queryset = Reading.objects.filter(id_sensor=Sensor.objects.get(pk=id_sensor))

        serializer = ReadingSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, id_sensor, format=None):
        read = Reading(id_sensor=Sensor.objects.get(id=id_sensor),
                       value=float(request.data.get("value", "0")))
        read.save()

        return Response(status=status.HTTP_201_CREATED)


#########################################################
# Alarms Settings per sensor
#########################################################

class AlarmsSettings_param(ListCreateAPIView):
    queryset = AlarmsSettings.objects.all()
    serializer_class = AlarmsSettingsSerializer

    def list(self, request, id_sensor):
        # Note the use of `get_queryset()` instead of `self.queryset`

        queryset = AlarmsSettings.objects.filter(id_sensor=Sensor.objects.get(pk=id_sensor))

        serializer = AlarmsSettingsSerializer(queryset, many=True)
        return Response(serializer.data)


#########################################################
# Alarms
#########################################################

class Alarms_param_reading(ListCreateAPIView):
    queryset = Alarms.objects.all()
    serializer_class = AlarmsSerializer

    def list(self, request, id_reading):
        # Note the use of `get_queryset()` instead of `self.queryset`

        queryset = Alarms.objects.filter(id_reading=id_reading)

        serializer = AlarmsSerializer(queryset, many=True)
        return Response(serializer.data)


class Alarms_param_sensor(ListCreateAPIView):
    queryset = Alarms.objects.all()
    serializer_class = AlarmsSerializer

    def list(self, request, id_sensor):
        # Note the use of `get_queryset()` instead of `self.queryset`

        queryset = Reading.objects.filter(id_sensor=Sensor.objects.get(pk=id_sensor))

        serializer = AlarmsSerializer(queryset, many=True)
        return Response(serializer.data)
