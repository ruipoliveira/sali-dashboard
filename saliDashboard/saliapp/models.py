from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class CommunicationType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    path_or_number = models.CharField(max_length=128)

    def __str__(self):
        return str(self.id) + str(self.name)


class ControllerModule(models.Model):
    id = models.AutoField(primary_key=True)
    id_communication = models.ForeignKey(CommunicationType, on_delete=models.CASCADE)
    id_by_create = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    status_cm = models.BooleanField(default=True)
    date_create = models.DateTimeField(default=datetime.now, blank=True)
    memory = models.IntegerField()
    localization_cm = models.CharField(max_length=128)
    baterry_cm = models.IntegerField()

    def __str__(self):
        return str(self.id) + str(self.name)


class CMPerUsers(models.Model):
    id_cm = models.ForeignKey(ControllerModule, on_delete=models.CASCADE)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "User: " + str(self.id_user) + "; CM: " + str(self.id_cm)


class SensorModule (models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    seding_time = models.IntegerField()
    status_sm = models.BooleanField(default=True)
    baterry_sm = models.IntegerField()
    localization_sm = models.CharField(max_length=128)

    def __str__(self):
        return str(self.id) + str(self.name)


class CommunicationTypePerSM(models.Model):
    id_sm = models.ForeignKey(ControllerModule, on_delete=models.CASCADE)
    id_communication_type = models.ForeignKey(CommunicationType, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id_sm) + str(self.id_communication_type)


class SMPerCM(models.Model):
    id_cm = models.ForeignKey(ControllerModule, on_delete=models.CASCADE)
    id_sm = models.ForeignKey(SensorModule, on_delete=models.CASCADE)

    def __str__(self):
        return "Controller: " + str(self.id_cm) + "; Module: " + str(self.id_sm)


class SensorType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    scale_value = models.CharField(max_length=10)

    def __str__(self):
        return str(self.id) + str(self.name)


class Sensor(models.Model):
    id = models.AutoField(primary_key=True)
    id_sensor_type = models.ForeignKey(SensorType, on_delete=models.CASCADE)
    id_sm = models.ForeignKey(SensorModule, on_delete=models.CASCADE)
    status_actuator = models.BooleanField(default=False)

    def __str__(self):
        return "SM: "+str(self.id_sm) + " Type: "+str(self.id_sensor_type)


class AlarmsSettings(models.Model):
    id = models.AutoField(primary_key=True)
    id_sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    max = models.FloatField(default=0.0)
    min = models.FloatField(default=0.0)
    msgMax = models.CharField(max_length=228)
    msgMin = models.CharField(max_length=228)

    def __str__(self):
        return "Sensor: "+str(self.id_sensor) + "| Max: "+str(self.max) + " Min: "+str(self.min)





class Reading(models.Model):
    id = models.AutoField(primary_key=True)
    id_sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    value = models.FloatField(default=0.0)
    date_time = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return str(self.id_sensor) + " | Valor lido:" + str(self.value) + " as " + str(self.date_time)


class Alarms(models.Model):
    id_reading = models.ForeignKey(Reading, on_delete=models.CASCADE)

    def __str__(self):
        return "Ocorreu alarme : " + str(self.id_reading)
