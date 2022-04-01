from django.db import models

# Create your models here.
class Client(models.Model):
    SECTOR_CHOICES = (
        ('0', 'ADMINISTRACIÓN Y GESTIÓN (OFICINAS Y DESPACHOS)'),
        ('1', 'AGRICULTURA Y GANADERÍA'),
        ('2', 'INDUSTRIA ALIMENTARIA'),
        ('3', 'COMERCIO'),
        ('4', 'EDUCACIÓN'),
        ('5', 'FINANZAS Y SEGUROS'),
        ('6', 'INFORMACIÓN, COMUNICACIÓN Y ARTES GRÁFICAS'),
        ('7', 'Otro...')
    )

    SIZE_CHOICES = (
        ('0', '1 - 10 empleados'),
        ('1', '11 - 50 empleados'),
        ('2', '51 - 100 empelados'),
        ('3', '101 - 200 empleados'),
        ('4', '201 o más empelados')
    )

    first_name = models.CharField('Nombres', max_length=50)
    last_name = models.CharField('Apellidos', max_length=50)
    phone_number = models.CharField('Telefono', max_length=50)
    email = models.EmailField('Correo electronico', max_length=254, unique=True)
    subdomain = models.CharField('Subdominio', max_length=20, unique=True)
    rfc = models.CharField('RFC', max_length=13)
    enterprise_name = models.CharField('Nombre de la empresa', max_length=100)
    enterprise_sector = models.CharField('Sector de la empresa', max_length=1, choices=SECTOR_CHOICES)
    enterprise_size = models.CharField('Tamaño de la empresa', max_length=1, choices=SIZE_CHOICES)
    address_country = models.CharField('País', max_length=50, default='México')
    address_state = models.CharField('Estado', max_length=50)
    address_city = models.CharField('Ciudad', max_length=50)
    address_neighborhood = models.CharField('Colonia', max_length=50)

    class Meta:
        verbose_name = 'Cliente'

    def __str__(self):
        return self.first_name