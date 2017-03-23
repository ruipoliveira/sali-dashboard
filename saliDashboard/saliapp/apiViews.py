from rest_framework import viewsets
from rest_framework.views import APIView

from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404


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


class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class CommunicationViewSet(viewsets.ModelViewSet):
    queryset = CommunicationType.objects.all()
    serializer_class = CommunicationTypeSerializer


#########################################################
# Communication Type
#########################################################

class CommunicationTypeList(APIView):
    def get(self, request, format=None):
        snippets = CommunicationType.objects.all()
        serializer = CommunicationTypeSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CommunicationTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommunicationType_by_id(APIView):
    def get_object(self, pk):
        try:
            return CommunicationType.objects.get(pk=pk)
        except CommunicationType.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        comm = self.get_object(pk)
        serializer = CommunicationTypeSerializer(comm)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        comm = self.get_object(pk)
        serializer = CommunicationTypeSerializer(comm, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CommunicationType_by_name(APIView):
    def get_object(self, name):
        try:
            return CommunicationType.objects.get(name__iexact=name)
        except CommunicationType.DoesNotExist:
            raise Http404

    def get(self, request, name, format=None):
        comm = self.get_object(name)
        serializer = CommunicationTypeSerializer(comm)
        return Response(serializer.data)

    def put(self, request, name, format=None):
        comm = self.get_object(name)
        serializer = CommunicationTypeSerializer(comm, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, name, format=None):
        comm = self.get_object(name)
        comm.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#########################################################
# Sensor Type
#########################################################

class SensorTypeList(APIView):
    def get(self, request, format=None):
        sensor = SensorType.objects.all()
        serializer = SensorSerializer(sensor, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CommunicationTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SensorType_by_id(APIView):
    def get_object(self, pk):
        try:
            return CommunicationType.objects.get(pk=pk)
        except CommunicationType.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        sensor = self.get_object(pk)
        serializer = CommunicationTypeSerializer(sensor)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        sensor = self.get_object(pk)
        serializer = CommunicationTypeSerializer(sensor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        sensor = self.get_object(pk)
        sensor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SensorType_by_name(APIView):
    def get_object(self, name):
        try:
            return SensorType.objects.get(name__iexact=name)
        except CommunicationType.DoesNotExist:
            raise Http404

    def get(self, request, name, format=None):
        sensor = self.get_object(name)
        serializer = SensorSerializer(sensor)
        return Response(serializer.data)

    def put(self, request, name, format=None):
        sensor = self.get_object(name)
        serializer = SensorSerializer(sensor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, name, format=None):
        sensor = self.get_object(name)
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


class User_by_id(APIView):
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = CommunicationTypeSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class User_by_username(APIView):
    def get_object(self, username):
        try:
            return User.objects.get(username__iexact=username)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, username, format=None):
        user = self.get_object(username)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, username, format=None):
        user = self.get_object(username)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, username, format=None):
        user = self.get_object(username)
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


#####################


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
