from django.contrib import admin

from .models import *

admin.site.register(CommunicationType)
admin.site.register(ControllerModule)
admin.site.register(CMPerUsers)
admin.site.register(SensorModule)
admin.site.register(SMPerCM)
admin.site.register(CommunicationTypePerSM)
admin.site.register(SensorType)
admin.site.register(Sensor)
admin.site.register(AlarmsSettings)
admin.site.register(Reading)
admin.site.register(Alarms)
admin.site.register(SecretKey)


