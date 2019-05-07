from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, 'index.html')

def Home(request):
    return render(request,'index.html')

def AboutUs(request):
    return render(request, 'about.html')

def Courses(request):
    return render(request,'courses.html')

def Join_us(request):
    return render(request,'join.html')

def Web_icon(request):
    return render(request,'icons.html')

def Shor_codes(request):
    return render(request,'codes.html')

def Gallery(request):
    return render(request,'gallery.html')


def Contact_us(request):
    return render(request,'contact.html')