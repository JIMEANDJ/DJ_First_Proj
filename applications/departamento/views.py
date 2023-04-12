from django.shortcuts import render
from django.views.generic import ListView, FormView
from .forms import NewDepartamentoForm
from .models import Departamento


class DepartamentoListView(ListView):
    template_name = "departamento/lista_departamento.html"
    model = Departamento
    context_object_name = 'departamentos'


class NewDepartamentoview(FormView):
        template_name = "departamento/newdepartament.html"
        form_class = NewDepartamentoForm
        success_url = '/'
    
        def form_valid(self, form):
            print ('********************************')
            return super(NewDepartamentoview, self).form_valid(form)





    

