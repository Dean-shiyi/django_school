from django.shortcuts import render
from django.http import HttpResponse
from .models import SchoolEvents, ClientsSay
from school_users.forms import UserLoginForm, RegisterForm, AdmisssionForm
# Create your views here.


def index(request):
    events = SchoolEvents.objects.all().order_by('-id')
    clientsays = ClientsSay.objects.all().order_by('-id')
    return render(request, 'index.html',
                  {'events': events,
                   'clientsays': clientsays,
                  })

def Home(request):
    events = SchoolEvents.objects.all().order_by('-id')
    clientsays = ClientsSay.objects.all().order_by('-id')
    return render(request, 'index.html',
                  {'events': events,
                   'clientsays': clientsays,
                  })

def AboutUs(request):
    return render(request, 'about.html')

def Courses(request):
    return render(request, 'courses.html')

def Join_us(request):
    return render(request, 'join.html',
                  {
                      'AdmisssionForm': AdmisssionForm,
                  })

def Web_icon(request):
    return render(request, 'icons.html')

def Shor_codes(request):
    return render(request, 'codes.html')

def Gallery(request):
    return render(request, 'gallery.html')

def Contact_us(request):
    return render(request, 'contact.html')

def Login(request):
    return render(request, 'login.html',
                  {'UserLoginForm': UserLoginForm,
                   })

def Register(request):
    return render(request, 'register.html',
                  {'RegisterForm': RegisterForm,
                  })


