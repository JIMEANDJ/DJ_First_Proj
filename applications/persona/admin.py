from django.contrib import admin
from .models import Empleado,Habilidades
# Register your models here.


admin.site.register(Habilidades)

class Empleadoadmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'departament',
        'job',
        'full_name', 
        'id' #'''se puede agregar una funcion que no este en el models definiendola abajo'''
    )
    #
    def full_name(self,obj): #obj toma todo lo que esta dentro del admin
        return obj.first_name + ' ' + obj.last_name
    
    #
    search_fields = ('first_name',)
    list_filter = ('job', 'habilidades','departament')
    filter_horizontal = ('habilidades',) 

   
admin.site.register(Empleado,Empleadoadmin)
