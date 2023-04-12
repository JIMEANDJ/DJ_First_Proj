from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView, DeleteView#models
from django.urls import reverse_lazy
from .models import Empleado
from applications.departamento.models import Departamento



class IncioView(TemplateView):
    #VISTA QUE CARGA LA PAGINA DE INICIO
    template_name = 'inicio.html'


# 1.-  lista de todods los empleados de la empresa
class Listallempleados(ListView):
    template_name = 'persona/list_all.html'
    paginate_by = 5
    context_object_name = 'lista'

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        lista = Empleado.objects.filter(
            first_name__icontains = palabra_clave
        )                
        return lista   
    

 # lista para agregar editar o eliminar en ADMINISTRAR  

class Listaempleados(ListView):
    template_name = 'persona/lista_empleados.html'
    paginate_by = 8
    ordering = 'first_name'
    context_object_name = 'lista'
    model = Empleado


# 2.- Listar todos los empleados que pertenecen a un area de la empresa 
class ListbyareaEmpleado(ListView):
    template_name = 'persona/listarea.html'
    context_object_name = 'porarea'

    def get_queryset(self):
        area = self.kwargs['shorname']      
        lista = Empleado.objects.filter(
            departament__short_name = area
        )
        return lista
# 3.- listar empleados por trabajo
# 4.- Listar los empleados por palabra clave 

class ListEmpleadosbykeyword(ListView):
    template_name = "persona/bykeyword.html"
    context_object_name = 'empleadokeyword'

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        lista = Empleado.objects.filter(
            first_name = palabra_clave
        )                
        return lista   
    
# 5.- listar las habilidades del empleado}
class ListahabilidadesEmpleado(ListView):
    template_name = 'persona/habilidades.html'
    context_object_name = 'habilidades'

    def get_queryset(self):
        empleado = Empleado.objects.get(id = 2)
        return empleado.habilidades.all()
    


class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "persona/detail_empleado.html"

    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context['titulo'] = 'Empleado del mes' 
        return context
    
class SuccessView(TemplateView):
    template_name = "persona/success.html"


class EmpleadoCreateView(CreateView):
    template_name = "persona/add.html"
    model = Empleado
    fields = ['first_name', 'last_name', 'job', 'departament', 'habilidades']
    success_url = reverse_lazy('persona_app:correcto')

    def form_valid(self, form):
        #logica del proceso
        empleado = form.save()
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()
        return super(EmpleadoCreateView, self).form_valid(form)



class EmpleadoUpdateView(UpdateView):
    template_name = "persona/update.html"
    model = Empleado    
    fields = ['first_name', 'last_name', 'job', 'departament', 'habilidades']
    success_url = reverse_lazy('persona_app:editar_empleados')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print('****************************')
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        #logica del proceso        
        return super(EmpleadoUpdateView, self).form_valid(form)
    

class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "persona/delete.html"
    success_url = reverse_lazy('persona_app:correcto')
