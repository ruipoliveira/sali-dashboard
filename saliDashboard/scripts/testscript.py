import time
from saliapp.models import *
from datetime import datetime
from django.utils import timezone
from random import randint


def run():
    while True:
        now = datetime.now()

        for i in Sensor.objects.all():
            red = Reading(id_sensor=i,
                          value=(randint(0, 100)),
                          date_time=now)

            red.save()

        print "I am a script"
        time.sleep(60)
