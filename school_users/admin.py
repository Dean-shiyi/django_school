from django.contrib import admin
from .models import MyUsers
# Register your models here.

class MyUserAdmin(admin.ModelAdmin):
    pass

admin.site.register(MyUsers,MyUserAdmin)