"""
Definition of urls for DjangoSalicornia.
"""

from datetime import datetime

import django.contrib.auth.views

from django.contrib import admin
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required
from rest_framework_swagger.views import get_swagger_view

from saliapp.views import *
from django.contrib.auth.views import login

from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from saliapp import views
from rest_framework import routers

login_forbidden = user_passes_test(lambda u: u.is_anonymous(), 'home')


router = routers.DefaultRouter()
router.register(r'cm', views.ControllerModuleViewSet)
router.register(r'sm', views.SensorModuleViewSet)
router.register(r'sensor', views.SensorViewSet)


schema_view = get_swagger_view(title='Pastebin API')


urlpatterns = [

    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^doc/$', schema_view),


    url(r'^$', login_forbidden(login), name="login"),
    url(r'^home/$', home, name='home'),

    url(r'^accounts/login/$', login),
    url(r'^logout/$', logout_page),

    url(r'^showusers/$', login_required(ShowUsers.as_view()), name='showusers'),

    url(r'^novo/$', views.addNewUser),
    url(r'^profile/$', views.changeprofile, name='profile'),

    url(r'^admin/', admin.site.urls),

   # url(r'^recoverpassword/', views.recoverpassword),

    # Add coisas

    url(r'^devices/cm/all/$', login_required(ShowDevices.as_view()), name="addcpu"),
    url(r'^addsensor/$', views.add_sensor, name="addsensor"),
    url(r'^addmodule/$', views.add_module, name="addmodule"),



    url(r'^deletecm/(?P<id_cpu>[-\w]+)/$', views.deletecm, name="deletecm"),

    url(r'^devices/cm/(?P<id_cm>[-\w]+)/$', login_required(ShowSensorModule.as_view()), name="showdetails"),

    url(r'^addsm/(?P<id_cm>[-\w]+)/$', views.addSensorModule, name="addsm"),

    url(r'^devices/cm/(?P<id_cm>[-\w]+)/sm/(?P<id_sm>[-\w]+)$', login_required(SensorValues.as_view()),
        name="viewSensors"),

    url(r'^typesensor/$', login_required(TypeSensor.as_view()), name="typesensor"),

    url(r'^typecommunication/$', login_required(TypeCommunication.as_view()), name="typecommunication"),

    url(r'^deletecomm/(?P<id_comm>[-\w]+)/$', views.deletecomm, name="deletecomm"),

    url(r'^deletesm/cm/(?P<id_cm>[-\w]+)/sm/(?P<id_sm>[-\w]+)$', views.deletesm, name="deletesm"),

    url(r'^deletesensor/(?P<id_sensor>[-\w]+)/$', views.deletesensor, name="deletesensor"),



    url(r'^deleteallarm/(?P<id_allarm>[-\w]+)/$', views.checkedAllarms, name="deleteallarm"),


    #url(r'^post1/$', views.post1, name="post1"),

    #API

#    url(r'^sensor/', views.SensorViewSet.as_view()),
#    url(r'^medicoes/', views.MeasureViewSet.as_view()),
#    url(r'^tudo/', views.SensorMeasurementsViewSet.as_view()),



]

#urlpatterns = format_suffix_patterns(urlpatterns)
handler404 = 'views.handler404'
handler500 = 'views.handler500'


