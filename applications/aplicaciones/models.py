from django.db import models

# Create your models here.
class Application(models.Model):
    name = models.CharField('Nombre', max_length=50)
    description = models.CharField('Descripción', max_length=50)

    class Meta:
        verbose_name = 'Aplicacion'
        verbose_name_plural = 'Aplicaciones'

    def __str__(self):
        return self.name