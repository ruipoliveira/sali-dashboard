"""
Definition of views.
"""
import csv
import datetime
import random
from django.contrib.auth.models import Group
from django.core.mail import send_mail

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
from .apiViews import *
from django.http import HttpResponse

# django_list = list(User.objects.all())

current_date_y_m_d = datetime.now().strftime('%Y-%m-%d')


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


class Register(View):
    def get(self, request, shortcode=None, *args, **kwargs):
        return render(request, 'registration/register.html', {
            'allCompany': Group.objects.get(name="company").user_set.all()
        })

    def post(self, request, shortcode=None, *args, **kwargs):
        # if User.objects.filter(username=request.POST["username"]).exists():
        #    messages.success(request, '\"' + request.POST["username"] + '\" deleted successfully!')
        #    return render(request, 'register')

        #if not User.objects.filter(username=request.POST["username"]).exists():
        #    messages.error(request, 'This username already exists!')
        #    return redirect('register')

        if request.POST["password1"] != request.POST["password2"]:
            messages.error(request, 'Passwords do not match!')
            return redirect('register')

        print request.POST["company"]


        # print request.POST["terms"]

        newUser = User.objects.create_user (username=request.POST["username"],
                       last_name=request.POST["last"],
                       first_name=request.POST["first"],
                       email=request.POST["email"],
                       password=request.POST["password1"]
                       )

        newUser.is_active = False

        newUser.save()

        company = User.objects.get(first_name=request.POST["company"])

        g = Group.objects.get(name='general')
        g.user_set.add(newUser)

        userpercompany = UserPerCompany(id_company=company,
                                        id_general_user=newUser)

        userpercompany.save()

        header = 'Novo utilizador registado associado a sua empresa '
        msg = 'Novo utilizador ' + newUser.username + ' registado. Aceda a sua conta para o validar.'

        send_mail(header, msg, 'ruipedrooliveira@ua.pt',
                  [company.email], fail_silently=False)

        return redirect('home')


def recover(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'registration/recover.html',
        {
            'title': 'roliveira',
            'year': datetime.now().year,
        }
    )


@login_required
def validate_user(request, id_user):
    user = User.objects.get(id=id_user)
    user.is_active = True
    user.save()

    header = 'Validacao do utilizador ' + user.username
    msg = 'Caro ' + user.first_name + ' ' + user.last_name + '\nO seu utilizador acabou de ser valiado pela sua empresa!'

    send_mail(header, msg, 'ruipedrooliveira@ua.pt',
              ['rui.oliveira.rpo@gmail.com'], fail_silently=False)

    messages.success(request, '\"' + str(user.username) + '\" validated successfully!')

    return redirect('managerUser')


@login_required
def remove_user(request, id_user):
    user = User.objects.get(id=id_user)
    user.delete()
    user.save()
    messages.success(request, '\"' + str(user.username) + '\" removed successfully!')
    return redirect('managerUser')


def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')


@login_required
def add_module(request):
    return render_to_response(
        'view/view_smodule.html', {
            'user': request.user,
            'title': 'Contact'
        })


@login_required
def add_sensor(request):
    return render_to_response(
        'view/view_sensor.html', {
            'user': request.user,
            'title': 'Contact'
        })


@login_required
def home(request):
    all_id_sensor = Reading.objects.all().values_list('id_sensor', flat=True)

    out_list = []
    for val in all_id_sensor:
        if not val in out_list:
            out_list.append(val)

    print out_list

    cenas = []
    for i in out_list:
        cenas.append(Reading.objects.filter(id_sensor=i).order_by('-date_time')[0])

    # Model.objects.

    print cenas

    # token = Token.objects.create(user=request.user)

    # print token.key


    return render_to_response(
        'home.html',
        {'user': request.user,
         'title': 'Dashboard',
         'titlesmall': 'Control panel',
         'allControllerM': ControllerModule.objects.all(),
         'allSensorM': SensorModule.objects.all(),
         'smpercm': SMPerCM.objects.all(),
         'allSensor': Sensor.objects.all(),
         'current_date': current_date_y_m_d,
         'allarms_settings': AlarmsSettings.objects.all(),
         'userregistrations': User.objects.all().count(),
         'SMregistrations': SensorModule.objects.all().count(),
         'CMregistrations': ControllerModule.objects.all().count(),
         'totalReadings': Reading.objects.all().count(),
         'allReadings': cenas,
         'allAlarms': Alarms.objects.all()
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
    messages.success(request, '\"' + str(u.name) + '\" deleted successfully!')
    u.delete()

    # messages.add_message(request, messages.INFO, 'Improve your profile today!')

    return redirect('addcpu')


@login_required
def checkedAllarms(request, id_allarm):
    d = Alarms.objects.get(id=id_allarm)
    d.checked = True
    d.save()

    return redirect('home')


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
def profile(request):

    try:
        company = UserPerCompany.objects.get(id_general_user=request.user).id_company.first_name
    except ObjectDoesNotExist:
        company = request.user.first_name

    return render_to_response(
        'changeProfile.html',{
            'user': request.user,
            'company': company,
            'token': Token.objects.get(user=request.user),
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

        return redirect('view/view_cmodule.html')
    else:
        return render_to_response('view/view_cmodule.html', context_instance=RequestContext(request))


# class Coisas(View):
#    def get(self, request, idCM, shortcode=None, *args, **kwargs):
#        return  redirect('addcpu')
#    def post(self, request, shortcode=None, *args, **kwargs):
#        return redirect('addcpu')



class SensorValues(View):
    def get(self, request, shortcode=None, *args, **kwargs):
        # get id_sm and id_cm
        id_sm = self.kwargs['id_sm']
        id_cm = self.kwargs['id_cm']
        date_start = self.kwargs['dates']
        date_finish = self.kwargs['datef']

        # , date_time__range=[self.date_start, self.date_finish]

        readWithFilter = Reading.objects.filter(id_sensor=id_sm, date_time__range=[date_start + ' 00:00:00',
                                                                                   date_finish + ' 23:59:59'])

        # avgReadWithFilter = readWithFilter.aggregate(Avg('value')).values()[0]
        # print avgReadWithFilter
        # print datetime.now

        time = []

        for f in Sensor.objects.filter(id_sm=id_sm):
            for r in Reading.objects.filter(id_sensor=f.id, date_time__range=[date_start + ' 00:00:00',
                                                                              date_finish + ' 23:59:59']):
                if r.date_time.strftime('%d/%m/%Y %H:%M') not in time:
                    time.append(r.date_time.strftime('%d/%m/%Y %H:%M'))

        time.sort()

        print time

        nrTotalMedicoes = len(time)

        name_sensors = []
        color_random = []
        id_sensor = []
        for a in Sensor.objects.filter(id_sm=id_sm):
            name_sensors.append(str(a.id_sensor_type.name) + " (" + str(a.id_sensor_type.scale_value) + ")")
            id_sensor.append(a.id)
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

            for x in Reading.objects.filter(id_sensor=i.id, date_time__range=[date_start + ' 00:00:00',
                                                                              date_finish + ' 23:59:59']).order_by(
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

        # calculate statistic


        maxValue = []
        minValue = []
        avg = []
        nrmeasure = []

        for i in final:
            if len(i) > 0:
                withoutnull = [x for x in i if isinstance(x, float)]
                # print withoutnull
                if len(withoutnull) != 0:
                    nrmeasure.append(len(withoutnull))
                    maxValue.append("{0:.3f}".format(max(withoutnull)))
                    minValue.append("{0:.3f}".format(min(withoutnull)))
                    avg.append("{0:.3f}".format(mean(withoutnull)))

        return render(request,
                      'view/view_sensor.html', {
                          'user': request.user,
                          'title': 'Data visualization',
                          'titlesmall': SensorModule.objects.get(id=id_sm).name +
                                        " of controller module " +
                                        ControllerModule.objects.get(id=id_cm).name,
                          'final': zip(name_sensors, id_sensor, color_random, final, nrmeasure, maxValue, minValue,
                                       avg),
                          'time_format': time,
                          'date_start': date_start,
                          'date_finish': date_finish,
                          'current_date': current_date_y_m_d,
                          'notData': len(time) == 0,
                          'maxvalue': maxValueAll,
                          'minValue': minValueAll,
                          'id_sm': id_sm,
                          'id_cm': id_cm
                      })

    def post(self, request, shortcode=None, *args, **kwargs):

        return redirect(request.path)


@login_required
def showalldata(request, id_sm, id_cm, dates, datef):
    allSensorID = map(int, Sensor.objects.filter(id_sm=id_sm).values_list('id', flat=True))

    print allSensorID

    return render(
        request,
        'view/viewAllData.html',
        dict(user=request.user, title='Dataset',
             titlesmall=SensorModule.objects.get(id=id_sm).name +
                        " of controller module " +
                        ControllerModule.objects.get(id=id_cm).name,
             datashow=Reading.objects.filter(id_sensor__in=allSensorID,
                                             date_time__range=[dates + ' 00:00:00',
                                                               datef + ' 23:59:59']).all(),
             id_sm=id_sm,
             id_cm=id_cm, ),

    )


@login_required
def exportcsv(request, id_sm, id_cm):
    import csv
    from django.utils.encoding import smart_str

    allSensorID = map(int, Sensor.objects.filter(id_sm=id_sm).values_list('id', flat=True))

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="sensor_' + datetime.now().strftime(
        "%Y-%m-%d_%H:%M:%S") + '.csv"'

    writer = csv.writer(response, csv.excel)

    response.write(u'\ufeff'.encode('utf8'))
    writer.writerow([
        smart_str(u"ID"),
        smart_str(u"Sensor type"),
        smart_str(u"Scale"),
        smart_str(u"Value"),
    ])
    for obj in Reading.objects.filter(id_sensor__in=allSensorID).all():
        writer.writerow([
            smart_str(obj.id),
            smart_str(obj.id_sensor.id_sensor_type.name),
            smart_str(obj.id_sensor.id_sensor_type.scale_value),
            smart_str(obj.value)
        ])

    return response


class ShowSensorModule(View):
    def get(self, request, shortcode=None, *args, **kwargs):
        id_cpu = self.kwargs['id_cm']

        x = SMPerCM.objects.filter(id_cm=id_cpu)
        y = [e.id_sm for e in x]

        print

        x1 = CommunicationTypePerSM.objects.filter(id_sm=id_cpu)
        print x1

        y1 = [e.id_communication_type for e in x1]
        print y1

        return render(request,
                      'view/view_smodule.html',
                      {'user': request.user,
                       'title': 'Sensor modules',
                       'titlesmall': ControllerModule.objects.get(id=id_cpu).name,
                       'id_cpu1': id_cpu,
                       'allSM': y,
                       'comm': y1,
                       'current_date': current_date_y_m_d,
                       'allAllarms': AlarmsSettings.objects.all(),
                       'notSM': len(y) == 0,
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

        if not request.POST["seding"]:
            seding = 10
        else:
            seding = request.POST["seding"]

        # criacao de uma instancia SM
        sm = SensorModule(name=request.POST["name"].replace("_", " "),
                          localization_sm="36.974,-122.025",
                          baterry_sm=100,
                          status_sm=status_sm,
                          seding_time=seding)
        sm.save()

        # adicionar SM a este CM
        smpercm = SMPerCM(id_sm=sm, id_cm=ControllerModule.objects.get(id=self.kwargs['id_cm']))
        smpercm.save()

        for comm in request.POST.getlist("communication"):
            print comm
            commPerSM = CommunicationTypePerSM(id_sm=sm,
                                               id_communication_type=CommunicationType.objects.get(name=comm))
            commPerSM.save()

        nrItemsSensor = request.POST["nritems"]

        sensor_req = Sensor(id_sm=sm, id_sensor_type=SensorType.objects.get(id=request.POST["sensors"]))
        sensor_req.save()

        sensor_allarms_req = AlarmsSettings(id_sensor=sensor_req,
                                            max=request.POST["max"],
                                            msgMax=request.POST["max_msg"],
                                            min=request.POST["min"],
                                            msgMin=request.POST["min_msg"])

        sensor_allarms_req.save()

        if int(nrItemsSensor) > 1:
            for i in range(1, int(nrItemsSensor)):
                sensor_req = Sensor(id_sm=sm,
                                    id_sensor_type=SensorType.objects.get(id=request.POST["sensors_" + str(i)]))
                sensor_req.save()

                sensor_allarms_req = AlarmsSettings(id_sensor=sensor_req,
                                                    max=request.POST["max_" + str(i)],
                                                    msgMax=request.POST["max_msg_" + str(i)],
                                                    min=request.POST["min_" + str(i)],
                                                    msgMin=request.POST["min_msg_" + str(i)])

                sensor_allarms_req.save()

        messages.success(request, '\"' + str(sm.name) + '\" created successfully!')

        return redirect('showdetails', id_cm=self.kwargs['id_cm'])


@login_required
def deletesm(request, id_cm, id_sm):
    u = SensorModule.objects.get(pk=id_sm)
    messages.success(request, '\"' + str(u.name) + '\" deleted successfully!')
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
                      'view/view_cmodule.html', {
                          'user': request.user,
                          'title': 'Controller module',
                          'titlesmall': 'All devices',
                          'allCPUs': allCPUs,
                          'notCm': allCPUs.count() == 0,
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

        if not request.POST["memory"]:
            memory = "0"
        else:
            memory = request.POST["memory"]

        cm = ControllerModule(id_communication=CommunicationType.objects.get(id=request.POST["comm"]),
                              id_by_create=self.request.user,
                              name=request.POST["name"].replace("_", " "),
                              status_cm=status,
                              memory=memory,
                              localization_cm="36.964,-122.015",
                              baterry_cm=100)
        cm.save()

        cmperuser = CMPerUsers(id_cm=cm, id_user=self.request.user)
        cmperuser.save()

        for manager in request.POST.getlist("managers"):
            print manager
            cmperusera = CMPerUsers(id_cm=cm, id_user=User.objects.get(username=manager))
            cmperusera.save()

        messages.success(request, '\"' + cm.name + '\" created successfully!')
        return redirect('addcpu')


class TypeSensor(View):
    def get(self, request, shortcode=None, *args, **kwargs):
        return render(request,
                      'add/typesensors.html', {
                          'user': request.user,
                          'title': 'Sensor type',
                          'titlesmall': 'All types',
                          'sensorAll': SensorType.objects.all(),
                          'notSensor': SensorType.objects.all().count() == 0,
                          'exist': Sensor.objects.filter(id_sensor_type=2).exists()
                      })

    def post(self, request, shortcode=None, *args, **kwargs):
        print request.POST['color']

        st = SensorType(name=request.POST["name"],
                        scale_value=request.POST["scale"],
                        image_path=request.POST["path"],
                        color="bg-" + request.POST['color'])
        messages.success(request, '\"' + str(st.name) + '\" created successfully!')
        st.save()

        return redirect('typesensor')


class TypeCommunication(View):
    def get(self, request, shortcode=None, *args, **kwargs):
        return render(request,
                      'add/typecommunication.html', {
                          'user': request.user,
                          'title': 'Type Communication',
                          'titlesmall': 'All types',
                          'notComm': CommunicationType.objects.all().count() == 0,
                          'commAll': CommunicationType.objects.all(),
                      })

    def post(self, request, shortcode=None, *args, **kwargs):
        ct = CommunicationType(name=request.POST["name"],
                               path_or_number=request.POST["source"],
                               image_path=request.POST["path"])

        messages.success(request, '\"' + str(ct.name) + '\" created successfully!')
        ct.save()

        return redirect('typecommunication')


@login_required
def deletecomm(request, id_comm):
    u = CommunicationType.objects.get(pk=id_comm)
    messages.success(request, '\"' + str(u.name) + '\" deleted successfully!')
    u.delete()

    # messages.add_message(request, messages.INFO, 'Improve your profile today!')

    return redirect('typecommunication')


@login_required
def deletesensor(request, id_sensor):
    print id_sensor
    u = SensorType.objects.get(pk=id_sensor)
    messages.success(request, '\"' + str(u.name) + '\" deleted successfully!')
    u.delete()

    # messages.add_message(request, messages.INFO, 'Improve your profile today!')

    return redirect('typesensor')


class ManagerUser(View):
    def get(self, request, shortcode=None, *args, **kwargs):
        return render(request,
                      'addusers.html', {
                          'user': request.user,
                          'title': 'User management',
                          'titlesmall': 'All types',
                          'userAll': UserPerCompany.objects.filter(id_company=request.user)
                      })

    def post(self, request, shortcode=None, *args, **kwargs):
        st = SensorType(name=request.POST["name"],
                        scale_value=request.POST["scale"],
                        image_path=request.POST["path"])
        messages.success(request, str(ct.name) + ' created successfully!')
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
