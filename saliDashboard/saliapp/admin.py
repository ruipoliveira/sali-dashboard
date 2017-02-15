from django.contrib import admin

from .models import CPUPerUsers, CPU, CommunicationType, Module, ModulePerCPU
from .models import SensorType, Sensor, SensorsPerModule, AlarmsSettings, Reading, Alarms

# Register your models here.
admin.site.register(CPUPerUsers)

admin.site.register(CPU)

admin.site.register(CommunicationType)

admin.site.register(Module)

admin.site.register(ModulePerCPU)

admin.site.register(SensorType)

admin.site.register(Sensor)

admin.site.register(SensorsPerModule)

admin.site.register(AlarmsSettings)

admin.site.register(Reading)

admin.site.register(Alarms)



