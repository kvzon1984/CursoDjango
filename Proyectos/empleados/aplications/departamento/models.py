from django.db import models

# Create your models here.
class Departamento(models.Model):
    name = models.CharField('Nombre', max_length=50)
    short_name = models.CharField('Nombre Corto', max_length=20, unique=True)
    anulate = models.BooleanField('Anulado', default = False)

    class Meta(object):
        verbose_name = 'Mis Depatamentos'
        verbose_name_plural = 'Mis Departamentos'
        ordering = ['id']
        


    
    def __str__(self):
        return str(self.id) + ' - ' + self.short_name + ' - ' + self.name

