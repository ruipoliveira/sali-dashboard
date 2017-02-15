"""
Definition of views.
"""
from django.shortcuts import render
from django.http import HttpRequest
from datetime import datetime

from saliapp.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from .models import CPU

"""
from rest_framework.views import APIView
from rest_framework.response import Response


from .models import Sensor, Measure, SensorMeasurements
from .serializers import SensorSerializer, MeasureSerializer, SensorMeasurementsSerializer


class SensorViewSet(APIView):
    def get(self, request):
        queryset = Sensor.objects.all()
        serializer = SensorSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self):
        pass


class MeasureViewSet(APIView):
    def get(self, request):
        queryset = Measure.objects.all()
        serializer = MeasureSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self):
        pass

class SensorMeasurementsViewSet(APIView):
    def get(self, request):
        queryset = SensorMeasurements.objects.all()
        serializer = SensorMeasurementsSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self):
        pass
"""

def home2(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title': 'roliveira',
            'year': datetime.now().year,
        }
    )


def recoverpassword(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'registration/recover.html',
        {
            'title': 'roliveira',
            'year': datetime.now().year,
        }
    )


@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
                email=form.cleaned_data['email']
            )
            return HttpResponseRedirect('/register/success/')
    else:
        form = RegistrationForm()
    variables = RequestContext(request, {
        'form': form
    })

    return render_to_response(
        'registration/register.html',
        variables,
    )


def addNewUser(resquest):
    new_user = User.objects.create_user(self.cleaned_data['username'],
                                        self.cleaned_data['email'],
                                        self.cleaned_data['password1'])
    new_user.first_name = self.cleaned_data['first_name']
    new_user.last_name = self.cleaned_data['last_name']
    new_user.save()

    return render(request, 'home.html');


def register_success(request):
    return render_to_response(
        'registration/success.html',
    )


def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')

@login_required
def add_cpu(request):
    return render_to_response(
        'add/addcpu.html', {
            'user': request.user,
            'title': 'Contact'
        })

@login_required
def add_module(request):
    return render_to_response(
        'add/addmodule.html', {
            'user': request.user,
            'title': 'Contact'
        })

@login_required
def add_sensor(request):
    return render_to_response(
        'add/addsensor.html', {
            'user': request.user,
            'title': 'Contact'
        })


@login_required
def home(request):
    return render_to_response(
        'home.html',
        {'user': request.user,
         'title': 'Contact',
         'obj': CPU.objects.all()
         })


@login_required
def newuser(request):

    return render_to_response(
        'addusers.html',
        {'user': request.user,
         'title': 'Contact'
         })


@login_required
def changeprofile(request):
    return render_to_response(
        'changeProfile.html',
        {'user': request.user,
         'title': 'New user'
         })