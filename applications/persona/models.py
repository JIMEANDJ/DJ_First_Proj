from django.db import models
from applications.departamento.models import Departamento



class Habilidades(models.Model):
    habilida = models.CharField('Habilidad', max_length=100)
    
    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = ' Habilidades Empleado'

    def __str__(self):
        return str(self.id) + '-' + self.habilida




# Create your models here.
class Empleado(models.Model):
    """modelo tabla empleado """
    job_choices = (
        ('0', 'Contador'),
        ('1', 'Administrador'),
        ('2', 'Economista'),
        ('3', 'Otro'),
    )
    #contador
    #administrador
    #econimista
    # otro
    first_name = models.CharField('nombres', max_length=60)
    last_name = models.CharField('apellidos', max_length=60)
    full_name = models.CharField('Nombre Completo', max_length=120, blank=True)
    job = models.CharField('Trabajo', max_length=50, choices=job_choices)
    departament = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    avatar  = models.ImageField(upload_to='empleado', blank=True, null=True)
    habilidades = models.ManyToManyField(Habilidades) 
    
 
    class Meta:
         verbose_name = 'Empleado'
         verbose_name_plural = 'Empleados de la empresa'
        
    
         
   
    # imagen models.ImageField(_(""), upload_to=None, height_field=None, width_field=None, max_length=None)

    def __str__(self):
        return str(self.id) + '-' + self.first_name + '-' + self.last_name
