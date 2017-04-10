from django.contrib import admin
from django.contrib.auth.models import Permission, ContentType

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

admin.site.register(Permission)
admin.site.register(ContentType)

admin.site.register(UserPerCompany)