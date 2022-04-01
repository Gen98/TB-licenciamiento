from django.contrib import admin
from .models import Client

# Register your models here.
class ClientAdmin(admin.ModelAdmin):
    list_display = (
        'enterprise_name',
        'rfc',
        'dominio',
        'contact',
        'email',
    )
    def contact(self, obj):
        return obj.first_name + ' ' + obj.last_name
    def dominio(slef, obj):
        return obj.subdomain + '.truebii.com'


admin.site.register(Client, ClientAdmin)