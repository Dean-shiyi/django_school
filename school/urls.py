"""school URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from school_views import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('index', views.index),
    url(r'^home/', views.Home, name='Home'),
    url(r'^about/', views.AboutUs, name='AboutUs'),
    url(r'^courses/', views.Courses, name='Courses'),
    url(r'^join_us/', views.Join_us, name='Join_us'),
    url(r'^web_icon/', views.Web_icon, name='Web_icon'),
    url(r'^short_codes/', views.Shor_codes, name='Short_codes'),
    url(r'^gallery/', views.Gallery, name='Gallery'),
    url(r'^contact_us/', views.Contact_us, name='Contact_us'),
]
