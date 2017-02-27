"""
Definition of views.
"""
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.datastructures import MultiValueDictKeyError
from django.views import View
from django.views.decorators.csrf import csrf_protect

from saliapp.forms import *
from .models import *

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


#django_list = list(User.objects.all())


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
         #'obj': CPU.objects.all()
         })


@login_required
def newuser(request):

    return render_to_response(
        'addusers.html',
        {'user': request.user,
         'title': 'Contact'
         })


#def deleteCPU(request, int id_delete):
#    CPU.objects.filter(id_delete=id).delete();
#    return ""

@login_required
def deletecm(request, id_cpu):
    u = ControllerModule.objects.get(pk=id_cpu)
    messages.success(request, str(u.name)+' Eliminado com sucesso!')
    u.delete()

    #messages.add_message(request, messages.INFO, 'Improve your profile today!')

    return redirect('addcpu')


@login_required
def showdetails(request, id_cpu):


    #messages.add_message(request, messages.INFO, 'Improve your profile today!')

    #print str(SMPerCM.objects)

    x = SMPerCM.objects.filter(id_cm=id_cpu)
    y = [e.id_sm for e in x]

    x1 = CommunicationTypePerSM.objects.filter(id_sm=id_cpu)
    print x1

    y1 = [e.id_communication_type for e in x1]
    print y1

    return render_to_response(
        'add/addmodule.html',
        {'user': request.user,
         'title': 'Contact',
         'id_cpu1': id_cpu,
         'allSM': y,
         'comm': y1,
         'sensor': Sensor.objects.all()
         })




@login_required
def viewSensors(request, id_cm, id_sm):

    return render_to_response(
        'add/addsensor.html',
        {'user': request.user,
         'title': 'Contact',
         'id_cpu': id_cm,
         'sensor': [e.id_sensor_type for e in Sensor.objects.filter(id_sm=id_sm)]
         })





@login_required
def editcpu(request, id):
    #+some code to check if New belongs to logged in user
    cpu = ControllerModule.objects.get(pk=id)
    cpu.name = "fs"
    return add_cpu(request)



@login_required
def changeprofile(request):
    return render_to_response(
        'changeProfile.html',
        {'user': request.user,
         'title': 'New user'
         })


def post_new(request):
    form = PostForm()
    return render(request, 'add/post_edit.html', {'form': form})


def foo(request):
    if request.method == "POST":
        usern = request.POST.get('username', '')
        print (usern)

        return redirect('add/addcpu.html')
    else:
        return render_to_response('add/addcpu.html', context_instance=RequestContext(request))


#class Coisas(View):
#    def get(self, request, idCM, shortcode=None, *args, **kwargs):
#        return  redirect('addcpu')
#    def post(self, request, shortcode=None, *args, **kwargs):
#        return redirect('addcpu')


class Cenas(View):

    def get(self, request, shortcode=None, *args, **kwargs):
        allCPUs = ControllerModule.objects.all()
        userAll = CMPerUsers.objects.all()

        communicationAll = CommunicationType.objects.all()
        form = PostForm()

        return render(request,
            'add/addcpu.html', {
                'user': request.user,
                'title': 'Contact',
                'allCPUs': allCPUs,
                'totaluser': User.objects.all(),
                'userAll': userAll,
                'communicationAll': communicationAll,
                'form': form
            })

    def post(self, request, shortcode=None, *args, **kwargs):
        try:
            if request.POST["status"] == "on":
                status = True
        except MultiValueDictKeyError:
            status = False

        print

        cm = ControllerModule(id_communication=CommunicationType.objects.get(id=1),
                              id_by_create= self.request.user,
                              name=request.POST["name"],
                              status_cm=status,
                              memory=request.POST["memory"],
                              localization_cm="4123123,32131231",
                              baterry_cm=100)
        cm.save()

        cmperuser = CMPerUsers(id_cm=cm, id_user=self.request.user)
        cmperuser.save()

        for manager in request.POST.getlist("managers"):
            print manager
            cmperusera = CMPerUsers(id_cm=cm, id_user=User.objects.get(username=manager))
            cmperusera.save()

        messages.success(request, cm.name + 'New cpu adicionado com sucesso!')
        return redirect('addcpu')