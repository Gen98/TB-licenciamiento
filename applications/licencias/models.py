from django.db import models
from applications.clientes.models import Client
from applications.aplicaciones.models import Application

# Create your models here.
class License(models.Model):
    name = models.CharField('Nombre', max_length=50)
    estatus = models.BooleanField('Activo', default=True)
    applications = models.ManyToManyField(Application)

    class Meta:
        verbose_name = 'Licencia'

    def __str__(self):
        return self.name

class Clients_Licenses(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    license = models.ForeignKey(License, on_delete=models.CASCADE)
    estatus = models.BooleanField('Activo', default=True)
    expiration_date = models.DateField('Fecha de expiración', auto_now=False, auto_now_add=False)
    ip_server = models.CharField('Dirección IP del servidor', max_length=20)
    server_access = models.CharField('Credenciales de acceso', max_length=255)

    class Meta:
        verbose_name = 'Licenciamiento'

    def __str__(self):
        return self.client.enterprise_name + ' - ' + self.license.name
