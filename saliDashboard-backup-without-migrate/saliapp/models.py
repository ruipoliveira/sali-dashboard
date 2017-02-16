from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from datetime import date


class CommunicationType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    path = models.CharField(max_length=128)

    def __str__(self):
        return str(self.id) + str(self.name)


class CPU(models.Model):
    id = models.AutoField(primary_key=True)
    id_communication = models.ForeignKey(CommunicationType, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    date_creation = models.IntegerField()
    status = models.IntegerField()
    localization = models.CharField(max_length=128)

    memory = models.IntegerField()

    def __str__(self):
        return str(self.id) + str(self.name)


class CPUPerUsers(models.Model):
    id_cpu = models.ForeignKey(CPU, on_delete=models.CASCADE)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "User: " + str(self.id_user) + "; CPU: " + str(self.id_cpu)


class Module (models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    state = models.IntegerField()

    def __str__(self):
        return str(self.id) + str(self.name)


class ModulePerCPU(models.Model):
    id_cpu = models.ForeignKey(CPU, on_delete=models.CASCADE)
    id_module = models.ForeignKey(Module, on_delete=models.CASCADE)

    def __str__(self):
        return "CPU: " + str(self.id_cpu) + "; Module: " + str(self.id_module)


class SensorType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    magnitude = models.CharField(max_length=128)

    def __str__(self):
        return str(self.id) + str(self.name)


class Sensor(models.Model):
    id = models.AutoField(primary_key=True)
    id_sensor_type = models.ForeignKey(SensorType, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id_sensor_type)


class SensorsPerModule(models.Model):
    id_module = models.ForeignKey(Module, on_delete=models.CASCADE)
    id_sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)

    def __str__(self):
        return "Module: " + str(self.id_module) + "; Sensor: " + str(self.id_sensor)


class AlarmsSettings(models.Model):
    id = models.AutoField(primary_key=True)
    id_sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    max = models.IntegerField()
    min = models.IntegerField()


class Reading(models.Model):
    id = models.AutoField(primary_key=True)
    id_sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    value = models.IntegerField()

    def __str__(self):
        return str(self.id_sensor)


class Alarms(models.Model):
    id = models.AutoField(primary_key=True)
    id_reading = models.ForeignKey(Reading, on_delete=models.CASCADE)
    value = models.IntegerField()

