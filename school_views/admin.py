from django.contrib import admin
from .models import SchoolEvents,ClientsSay
# Register your models here.

class SchoolEventsAdmin(admin.ModelAdmin):
    pass

class ClientSayAdmin(admin.ModelAdmin):
    pass


admin.site.register(SchoolEvents, SchoolEventsAdmin)
admin.site.register(ClientsSay, ClientSayAdmin)