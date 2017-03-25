"""
Definition of urls for DjangoSalicornia.
"""

from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.views import login
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view

from saliapp import views
from saliapp.views import *

login_forbidden = user_passes_test(lambda u: u.is_anonymous(), 'home')

#router = routers.DefaultRouter()
#router.register(r'cm', views.ControllerModuleViewSet)
#router.register(r'sm', views.SensorModuleViewSet)
#router.register(r'sensor', views.SensorViewSet)
#router.register(r'comm', views.CommunicationViewSet)
#router.register(r'user', views.UserViewSet)



schema_view = get_swagger_view(title='API documentation')


urlpatterns = [

    #url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/doc/$', schema_view),


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

    url(r'^devices/cm/(?P<id_cm>[-\w]+)/sm/(?P<id_sm>[-\w]+)/date/(?P<date>[-\w]+)$', login_required(SensorValues.as_view()),
        name="viewSensors"),

    url(r'^typesensor/$', login_required(TypeSensor.as_view()), name="typesensor"),

    url(r'^typecommunication/$', login_required(TypeCommunication.as_view()), name="typecommunication"),

    url(r'^deletecomm/(?P<id_comm>[-\w]+)/$', views.deletecomm, name="deletecomm"),

    url(r'^deletesm/cm/(?P<id_cm>[-\w]+)/sm/(?P<id_sm>[-\w]+)$', views.deletesm, name="deletesm"),

    url(r'^deletesensor/(?P<id_sensor>[-\w]+)/$', views.deletesensor, name="deletesensor"),

    url(r'^deleteallarm/(?P<id_allarm>[-\w]+)/$', views.checkedAllarms, name="deleteallarm"),


    url(r'^devices/cm/(?P<id_cm>[-\w]+)/sm/(?P<id_sm>[-\w]+)/showalldata/$', views.showalldata, name="showalldata"),

    url(r'^devices/cm/(?P<id_cm>[-\w]+)/sm/(?P<id_sm>[-\w]+)/export/$', views.exportcsv, name="exportcsv"),


    #url(r'^post1/$', views.post1, name="post1"),

    #API

#    url(r'^sensor/', views.SensorViewSet.as_view()),
#    url(r'^medicoes/', views.MeasureViewSet.as_view()),
#    url(r'^tudo/', views.SensorMeasurementsViewSet.as_view()),


    url(r'^api/users/', views.ControllerModuleViewSet.as_view()),

    #communication type
    url(r'^api/communication/$', views.CommunicationTypeList.as_view()),
    url(r'^api/communication/(?P<pk_or_name>[-\w]+)/$', views.CommunicationType_param.as_view(), name='comm_type'),

    #sensor type
    url(r'^api/sensortype/$', views.SensorTypeList.as_view()),
    url(r'^api/sensortype/(?P<pk_or_name>[-\w]+)/$', views.SensorType_param.as_view()),


    # user
    url(r'^api/user/$', views.UserList.as_view(), name='user'),
    url(r'^api/user_id/(?P<pk>[0-9]+)/$', views.User_by_id.as_view(), ),
    url(r'^api/user_username/(?P<username>[-\w]+)/$', views.User_by_username.as_view()),

    # cm
    url(r'^api/cm/$', views.ControllerModuleList.as_view()),
    url(r'^api/cm_id/(?P<pk>[0-9]+)/$', views.ControllerModule_by_id.as_view(), ),
    url(r'^api/cm_name/(?P<name>[-\w]+)/$', views.ControllerModule_by_name.as_view()),

    # sm
    url(r'^api/sm/$', views.SensorModuleList.as_view()),
    url(r'^api/sm/(?P<pk_or_name>[-\w]+)/$', views.SensorModule_param.as_view()),

    #sm per cm
    url(r'^api/smpercm/$', views.SMperCMList.as_view()),
    url(r'^api/smpercm/(?P<pk_or_name_cm>[-\w]+)$', views.SMperCM_param.as_view()),

    #sensor
    url(r'^api/sensor/$', views.SensorList.as_view()),
    url(r'^api/sensor/(?P<pk_or_sensor_type>[-\w]+)$', views.Sensor_param.as_view()),


    #sensor per sm
    url(r'^api/sensorpersm/(?P<id_sm_or_name_sm>[-\w]+)$', views.SensorperSM_param.as_view()),


    #reading
    url(r'^api/reading/(?P<id_sensor>[0-9]+)/(?P<date_start>[-\w]+)/(?P<date_end>[-\w]+)$',
        views.Reading_param.as_view()),

    # allarms settings
    url(r'^api/allarmssettings/(?P<id_sensor>[0-9]+)$', views.AllarmsSettings_param.as_view()),


]

#urlpatterns = format_suffix_patterns(urlpatterns)
handler404 = 'views.handler404'
handler500 = 'views.handler500'


