from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView

from .models import Prueba
# import models

from .forms import Pruebaform

class Index(TemplateView):
    template_name = 'home/home.html'


#FOUNDATION

class ResumeFoundationView(TemplateView):
    template_name = 'home/resume_foundation.html'

    


class Prueba_listview(ListView):
    template_name = "home/lista.html"
    queryset = ['a' , 'b', 'c']
    context_object_name  = 'lista_prueba'
    
    
    
class ModeloPruebaListView(ListView):
    model = Prueba 
    template_name = "home/pruebas.html"
    context_object_name = 'lista_prueba'





class PruebaCreateView(CreateView):
    template_name = "home/add.html"
    model =Prueba
    form_class = Pruebaform
    success_url = '/'