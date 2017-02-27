"""
Definition of urls for DjangoSalicornia.
"""

from datetime import datetime

import django.contrib.auth.views

from django.contrib import admin
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required

from saliapp.views import *
from django.contrib.auth.views import login

from django.conf.urls import url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from saliapp import views

login_forbidden = user_passes_test(lambda u: u.is_anonymous(), 'home')


urlpatterns = [
    url(r'^$', login_forbidden(login), name="login"),
    url(r'^home/$', home, name='home'),

    url(r'^accounts/login/$', login),
    url(r'^logout/$', logout_page),

    url(r'^addusers/$', views.newuser),

    url(r'^novo/$', views.addNewUser),
    url(r'^changeprofile/$', views.changeprofile),

    url(r'^admin/', admin.site.urls),

   # url(r'^recoverpassword/', views.recoverpassword),

    # Add coisas

    url(r'^devices/cm/all$',  login_required(Cenas.as_view()), name="addcpu"),
    url(r'^addsensor/$', views.add_sensor, name="addsensor"),
    url(r'^addmodule/$', views.add_module, name="addmodule"),



    url(r'^deletecm/(?P<id_cpu>[-\w]+)/$', views.deletecm, name="deletecm"),

    url(r'^devices/cm/(?P<id_cpu>[-\w]+)/$', views.showdetails, name="showdetails"),

    url(r'^devices/cm/(?P<id_cm>[-\w]+)/sm/(?P<id_sm>[-\w]+)$', views.viewSensors, name="viewSensors"),

    #url(r'^post1/$', views.post1, name="post1"),

    #API

#    url(r'^sensor/', views.SensorViewSet.as_view()),
#    url(r'^medicoes/', views.MeasureViewSet.as_view()),
#    url(r'^tudo/', views.SensorMeasurementsViewSet.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)
