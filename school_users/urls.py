from django.conf.urls import url
from .views import user_login, user_register, user_logout, user_admission
urlpatterns = [
    url(r'^login/', user_login, name='login'),
    url(r'^register/', user_register, name='register'),
    url(r'^logout/', user_logout, name='logout'),
    url(r'^admisssion/', user_admission, name='admission'),
]
