from django.contrib import admin
from django.urls import path
from . import views

app_name = "departamento_app"
urlpatterns = [
    path ('lista-departamento/', views.DepartamentoListView.as_view(), name = 'departamento_list'),
    path ('new-departament/', views.NewDepartamentoview.as_view(), name = 'nuevo_departamento'),

   
]



