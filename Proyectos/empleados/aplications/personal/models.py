from django.db import models
from aplications.departamento.models import Departamento
from ckeditor.fields import RichTextField

# Create your models here.
class Habilidades(models.Model):
    habilidad = models.CharField('habilidad', max_length=50)

    class Meta(object):
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades Empleados'
        
    def __str__(self):
        return self.habilidad


class Empleados(models.Model):

    JOB_CHOICES = (
        ('0', 'CONTADOR'),
        ('1', 'ADMINISTRADOR'),
        ('2', 'ECONOMISTA'),
        ('3', 'DESARROLLADOR')
    )

    first_name = models.CharField('Nombres', max_length=60, help_text='Nombre')
    last_name = models.CharField('Apellidos', max_length=60, help_text='apellido')
    full_name = models.CharField('Nombre Completo', max_length=60,blank=True)
    job = models.CharField('Trabajo', max_length=50, choices= JOB_CHOICES)
    departamento_id = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    # avatar = models.ImageField('Imagen', upload_to='empleado', blank= True, null=True)
    habilidades = models.ManyToManyField(Habilidades)
    hoja_vida = RichTextField()

    class Meta(object):
        verbose_name = 'Empleados'
        verbose_name_plural = 'Mis Empleados'

    def __str__(self):
        return str(self.id) + ' - ' + self.first_name + ' - ' + self.last_name + ' - ' + self.job 

