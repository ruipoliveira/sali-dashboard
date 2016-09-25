"""
Definition of urls for DjangoSalicornia.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

from django.contrib import admin
from app.views import *
from django.contrib.auth.views import login

from django.contrib.auth.decorators import user_passes_test

import app.views

# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin
# admin.autodiscover()

login_forbidden =  user_passes_test(lambda u: u.is_anonymous(), 'home')

urlpatterns = [
    # Examples:
    
    url(r'^$', login_forbidden(login), name="login"),

    url(r'^home/$', home, name='home'),

    url(r'^accounts/login/$', login),
    url(r'^logout/$', logout_page),

    url(r'^addusers/$', app.views.newuser),

    url(r'^novo/$', app.views.addNewUser),

    url(r'^changeprofile/$', app.views.changeprofile),

    url(r'^admin/', include(admin.site.urls)),
]
