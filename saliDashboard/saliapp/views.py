"""
Definition of views.
"""
import datetime
import random

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
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from statistics import mean


from saliapp.forms import *
from .models import *


from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import *


class ControllerModuleViewSet(viewsets.ModelViewSet):
    queryset = ControllerModule.objects.all()
    serializer_class = ControllerModuleSerializer


class SensorModuleViewSet(viewsets.ModelViewSet):
    queryset = SensorModule.objects.all()
    serializer_class = SensorModuleSerializer


class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer



# django_list = list(User.objects.all())


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
        'view/viewmodule.html', {
            'user': request.user,
            'title': 'Contact'
        })


@login_required
def add_sensor(request):
    return render_to_response(
        'view/viewsensor.html', {
            'user': request.user,
            'title': 'Contact'
        })


@login_required
def home(request):
    return render_to_response(
        'home.html',
        {'user': request.user,
         'title': 'Dashboard',
         'titlesmall': 'Control panel',
         'allControllerM': ControllerModule.objects.all(),
         'allSensorM': SensorModule.objects.all(),
         'smpercm': SMPerCM.objects.all(),
         'allSensor': Sensor.objects.all(),
         'userregistrations': User.objects.all().count(),
         'SMregistrations': SensorModule.objects.all().count(),
         'CMregistrations': ControllerModule.objects.all().count(),
         'totalReadings': Reading.objects.all().count()
         # 'obj': CPU.objects.all()
         })


@login_required
def newuser(request):
    return render_to_response(
        'addusers.html',
        {'user': request.user,
         'title': 'Contact'
         })


# def deleteCPU(request, int id_delete):
#    CPU.objects.filter(id_delete=id).delete();
#    return ""

@login_required
def deletecm(request, id_cpu):
    u = ControllerModule.objects.get(pk=id_cpu)
    messages.success(request, str(u.name) + ' Eliminado com sucesso!')
    u.delete()

    # messages.add_message(request, messages.INFO, 'Improve your profile today!')

    return redirect('addcpu')


@csrf_exempt
def addSensorModule(request, id_cm):
    print "yooobrooo"
    return redirect('showdetails', id_cm=id_cm)


@login_required
def editcpu(request, id):
    # +some code to check if New belongs to logged in user
    cpu = ControllerModule.objects.get(pk=id)
    cpu.name = "fs"
    return add_cpu(request)


@login_required
def changeprofile(request):
    return render_to_response(
        'changeProfile.html',
        {'user': request.user,
         'title': 'Profile',
         'titlesmall': 'user',
         })


def post_new(request):
    form = PostForm()
    return render(request, 'view/post_edit.html', {'form': form})


def foo(request):
    if request.method == "POST":
        usern = request.POST.get('username', '')
        print (usern)

        return redirect('view/addcpu.html')
    else:
        return render_to_response('view/addcpu.html', context_instance=RequestContext(request))


# class Coisas(View):
#    def get(self, request, idCM, shortcode=None, *args, **kwargs):
#        return  redirect('addcpu')
#    def post(self, request, shortcode=None, *args, **kwargs):
#        return redirect('addcpu')


ola = True


class SensorValues(View):
    if ola:
        date_start = datetime.now().strftime("%Y-%m-%d")
        date_finish = datetime.now().strftime("%Y-%m-%d")
        print date_start
        ola = False

    def get(self, request, shortcode=None, *args, **kwargs):
        # Step 1: Create a DataPool with the data we want to retrieve.

        id_sm = self.kwargs['id_sm']
        id_cm = self.kwargs['id_cm']
        # , date_time__range=[self.date_start, self.date_finish]

        readWithFilter = Reading.objects.filter(id_sensor=id_sm,
                                                date_time__range=[self.date_start + ' 00:00:00',
                                                                  self.date_finish + ' 23:59:59'])

        # avgReadWithFilter = readWithFilter.aggregate(Avg('value')).values()[0]
        # print avgReadWithFilter
        # print datetime.now

        time = []

        for f in Sensor.objects.filter(id_sm=id_sm):
            for r in Reading.objects.filter(id_sensor=f.id, date_time__range=[self.date_start + ' 00:00:00',
                                                                              self.date_finish + ' 23:59:59']):
                if r.date_time.strftime('%d/%m/%Y %H:%M') not in time:
                    time.append(r.date_time.strftime('%d/%m/%Y %H:%M'))

        time.sort()

        print time

        nrTotalMedicoes = len(time)

        name_sensors = []
        color_random = []
        for a in Sensor.objects.filter(id_sm=id_sm):
            name_sensors.append(str(a.id_sensor_type.name) + " (" + str(a.id_sensor_type.scale_value) + ")")
            r = lambda: random.randint(0, 255)
            color_random.append('#%02X%02X%02X' % (r(), r(), r()))

        print name_sensors
        print color_random

        nrSensor = Sensor.objects.filter(id_sm=id_sm).count()

        # final = [['null'] * nrTotalMedicoes] * nrSensor  #

        # final = [['null', 'null', 'null', 'null'], ['null', 'null', 'null', 'null'], ['null', 'null', 'null', 'null'] ]

        final = [['null'] * nrTotalMedicoes for _ in range(nrSensor)]

        print final
        # print type(x)



        k0 = 0
        maxValueAll = 0
        minValueAll = 0
        for i in Sensor.objects.filter(id_sm=id_sm):
            print "#" + str(i.id) + " type:" + str(i.id_sensor_type.name)

            for x in Reading.objects.filter(id_sensor=i.id,
                                            date_time__range=[self.date_start + ' 00:00:00',
                                                              self.date_finish + ' 23:59:59']).order_by(
                'date_time'):
                # for a in reversed(time_format):
                #    if a == x.date_time.strftime('%d/%m/%Y %H:%M'):
                #        print a
                #        print x.value

                print str(x.date_time.strftime('%d/%m/%Y %H:%M')) + " value: " + str(x.value)

                for idx, d in enumerate(time):
                    if d == x.date_time.strftime('%d/%m/%Y %H:%M'):
                        final[k0][idx] = x.value  # ) + " i "+str(idx)
                        print k0
                        if x.value >= maxValueAll:
                            maxValueAll = x.value
                        if x.value <= minValueAll:
                            minValueAll = x.value

                print final
            k0 += 1


        #calculate statistic


        maxValue = []
        minValue = []
        avg = []
        nrmeasure = []

        for i in final:
            if len(i) >0:
                withoutnull = [x for x in i if isinstance(x, float)]
                #print withoutnull
                if len(withoutnull) !=0:
                    nrmeasure.append(len(withoutnull))
                    maxValue.append("{0:.3f}".format(max(withoutnull)))
                    minValue.append("{0:.3f}".format(min(withoutnull)))
                    avg.append("{0:.3f}".format(mean(withoutnull)))




        return render(request,
                      'view/viewsensor.html', {
                          'user': request.user,
                          'title': 'Data visualization',
                          'titlesmall': SensorModule.objects.get(
                              id=id_sm).name + " of controller module " + ControllerModule.objects.get(id=id_cm).name,
                          'avg': 12,
                          'id_cpu': id_cm,
                          'final': zip(name_sensors, final, color_random),
                          'maxvalue': maxValueAll,
                          'minValue': minValueAll,
                          'time_format': time,
                          'statistic': zip(name_sensors, nrmeasure, maxValue, minValue, avg),
                          # 'time_x': time_format,
                          'sensor': [e.id_sensor_type for e in Sensor.objects.filter(id_sm=id_sm)]
                      })

    def post(self, request, shortcode=None, *args, **kwargs):
        print request.POST["rangedate"]

        xs = request.POST["rangedate"].split(' - ')[0]
        xf = request.POST["rangedate"].split(' - ')[1]

        # x1 = datetime.datetime.strptime(xs, "%m/%d/%Y")

        xss = xs.split('/')
        xff = xf.split('/')

        # Y-m-d
        self.date_start = str(xss[2]) + '-' + str(xss[0]) + '-' + str(xss[1])
        self.date_finish = str(xss[2]) + '-' + str(xss[0]) + '-' + str(xss[1])

        return redirect(request.path)


class ShowSensorModule(View):
    def get(self, request, shortcode=None, *args, **kwargs):
        id_cpu = self.kwargs['id_cm']

        x = SMPerCM.objects.filter(id_cm=id_cpu)
        y = [e.id_sm for e in x]

        x1 = CommunicationTypePerSM.objects.filter(id_sm=id_cpu)
        print x1

        y1 = [e.id_communication_type for e in x1]
        print y1

        return render(request,
                      'view/viewmodule.html',
                      {'user': request.user,
                       'title': 'Sensor modules',
                       'titlesmall': ControllerModule.objects.get(id=id_cpu).name,
                       'id_cpu1': id_cpu,
                       'allSM': y,
                       'comm': y1,
                       'sensor': Sensor.objects.all(),
                       'sensortype': SensorType.objects.all(),
                       'commtype': CommunicationType.objects.all(),
                       'commPerSM': CommunicationTypePerSM.objects.all()
                       })

    def post(self, request, shortcode=None, *args, **kwargs):
        try:
            if request.POST["status"] == "on":
                status_sm = True
        except MultiValueDictKeyError:
            status_sm = False

        # criacao de uma instancia SM
        sm = SensorModule(name=request.POST["name"],
                          localization_sm="3243242432423,423423432423432",
                          baterry_sm=80,
                          status_sm=status_sm,
                          seding_time=request.POST["seding"],
                          )
        sm.save()

        # adicionar SM a este CM
        smpercm = SMPerCM(id_sm=sm, id_cm=ControllerModule.objects.get(id=self.kwargs['id_cm']))
        smpercm.save()

        for comm in request.POST.getlist("communication"):
            print comm
            commPerSM = CommunicationTypePerSM(id_sm=sm,
                                               id_communication_type=CommunicationType.objects.get(name=comm))
            commPerSM.save()

        for sensor in request.POST.getlist("sensors"):
            print sensor
            sensor = Sensor(id_sm=sm, id_sensor_type=SensorType.objects.get(name=sensor))
            sensor.save()

        return redirect('showdetails', id_cm=self.kwargs['id_cm'])


@login_required
def deletesm(request, id_cm, id_sm):
    u = SensorModule.objects.get(pk=id_sm)
    messages.success(request, str(u.name) + ' eliminado com sucesso!')
    u.delete()

    # messages.add_message(request, messages.INFO, 'Improve your profile today!')

    return redirect('showdetails', id_cm=id_cm)


class ShowDevices(View):
    def get(self, request, shortcode=None, *args, **kwargs):
        allCPUs = ControllerModule.objects.all()
        userAll = CMPerUsers.objects.all()

        communicationAll = CommunicationType.objects.all()
        form = PostForm()

        return render(request,
                      'view/addcpu.html', {
                          'user': request.user,
                          'title': 'Controller module',
                          'titlesmall': 'All devices',
                          'allCPUs': allCPUs,
                          'totaluser': User.objects.all(),
                          'userAll': userAll,
                          'communicationAll': communicationAll
                      })

    def post(self, request, shortcode=None, *args, **kwargs):
        try:
            if request.POST["status"] == "on":
                status = True
        except MultiValueDictKeyError:
            status = False

        cm = ControllerModule(id_communication=CommunicationType.objects.get(id=request.POST["comm"]),
                              id_by_create=self.request.user,
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


class TypeSensor(View):
    def get(self, request, shortcode=None, *args, **kwargs):
        return render(request,
                      'add/typesensors.html', {
                          'user': request.user,
                          'title': 'Type sensor',
                          'titlesmall': 'All types',
                          'sensorAll': SensorType.objects.all(),
                          'exist': Sensor.objects.filter(id_sensor_type=2).exists()

                      })

    def post(self, request, shortcode=None, *args, **kwargs):
        st = SensorType(name=request.POST["name"],
                        scale_value=request.POST["scale"],
                        image_path=request.POST["path"])
        messages.success(request, str(ct.name) + ' adicionado com sucesso!')
        st.save()

        return redirect('typesensor')


class TypeCommunication(View):
    def get(self, request, shortcode=None, *args, **kwargs):
        return render(request,
                      'add/typecommunication.html', {
                          'user': request.user,
                          'title': 'Type Communication',
                          'titlesmall': 'All types',
                          'commAll': CommunicationType.objects.all(),
                      })

    def post(self, request, shortcode=None, *args, **kwargs):
        ct = CommunicationType(name=request.POST["name"],
                               path_or_number=request.POST["source"],
                               image_path=request.POST["path"])

        messages.success(request, str(ct.name) + ' adicionado com sucesso!')
        ct.save()

        return redirect('typecommunication')


@login_required
def deletecomm(request, id_comm):
    u = CommunicationType.objects.get(pk=id_comm)
    messages.success(request, str(u.name) + ' eliminado com sucesso!')
    u.delete()

    # messages.add_message(request, messages.INFO, 'Improve your profile today!')

    return redirect('typecommunication')


@login_required
def deletesensor(request, id_sensor):
    print id_sensor
    u = SensorType.objects.get(pk=id_sensor)
    messages.success(request, str(u.name) + ' eliminado com sucesso!')
    u.delete()

    # messages.add_message(request, messages.INFO, 'Improve your profile today!')

    return redirect('typesensor')


class ShowUsers(View):
    def get(self, request, shortcode=None, *args, **kwargs):
        return render(request,
                      'addusers.html', {
                          'user': request.user,
                          'title': 'User management',
                          'titlesmall': 'All types',
                          'userAll': User.objects.all(),
                          'exist': Sensor.objects.filter(id_sensor_type=2).exists()

                      })

    def post(self, request, shortcode=None, *args, **kwargs):
        st = SensorType(name=request.POST["name"],
                        scale_value=request.POST["scale"],
                        image_path=request.POST["path"])
        messages.success(request, str(ct.name) + ' adicionado com sucesso!')
        st.save()

        return redirect('showusers')


########################################################################################
###################### Services used by controler module (CM) ##########################
########################################################################################

def firstConfiguration(request, nameCM):
    form = PostForm()
    return render(request, 'view/post_edit.html', {'form': form})


def updateConfiguration(request):
    form = PostForm()
    return render(request, 'view/post_edit.html', {'form': form})


def sendRedings(request):
    form = PostForm()

    return render(request, 'view/post_edit.html', {'form': form})


def handler404(request):
    response = render_to_response('error/404.html', {}, context_instance=RequestContext(request))
    response.status_code = 404
    return response


def handler500(request):
    response = render_to_response('error/500.html', {}, context_instance=RequestContext(request))
    response.status_code = 500
    return response
