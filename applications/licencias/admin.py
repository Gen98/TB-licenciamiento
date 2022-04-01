from django.contrib import admin
from .models import *
from .forms import ClientsLicensesForm

class LicenseAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'estatus'
    )

class ClientsLicensesAdmin(admin.ModelAdmin):
    list_display = (
        'client',
        'license',
        'estatus',
        'expiration_date',
        'ip_server'
    )
    form = ClientsLicensesForm

# Register your models here.
admin.site.register(License, LicenseAdmin)
admin.site.register(Clients_Licenses, ClientsLicensesAdmin)