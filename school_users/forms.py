from django import forms
from django.contrib.auth import get_user_model
from .models import AdmissionInfo
MyUser = get_user_model()


class UserLoginForm(forms.Form):
    name = forms.CharField(max_length=25, min_length=4)
    password = forms.CharField(max_length=255, min_length=6, widget=forms.PasswordInput())


class RegisterForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ("username", "password")
        widgets = {
            "password": forms.PasswordInput()
        }


class AdmisssionForm(forms.ModelForm):
    class Meta:
        model = AdmissionInfo
        fields = ('name',
                  'birth',
                  'gender',
                  'Email',
                  'Phone',
                  'course',
                  'course_time',
                  'addr',
                  'line',
                  'city',
                  'zip_code')
