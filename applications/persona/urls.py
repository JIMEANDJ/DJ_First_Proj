from django.contrib import admin
from django.urls import path
from . import views


app_name="persona_app"

urlpatterns = [    
    path('', views.IncioView.as_view(), name = 'inicio'),
    path('listar-todos-empleados/', views.Listallempleados.as_view(), name = 'listar_empleados'),
    path('listar-empleados-admin/', views.Listallempleados.as_view(), name = 'editar_empleados'),
    path('list-por-area/<shorname>/', views.ListbyareaEmpleado.as_view(), name = 'empleados_por_area'),  
    path('buscar-empleado/', views.ListEmpleadosbykeyword.as_view()),
    path('habilidades-empleado/', views.ListahabilidadesEmpleado.as_view()), 
    path('ver-empleado/<pk>/', views.EmpleadoDetailView.as_view(), name = "empleado_detail"), 
    path('add-empleado/', views.EmpleadoCreateView.as_view()), 
    path('success/', views.SuccessView.as_view(), name= 'correcto'),
    path('update-empleado/<pk>/', views.EmpleadoUpdateView.as_view(), name= 'modificar-empleado'),
    path('delete-empleado/<pk>/', views.EmpleadoDeleteView.as_view(), name= 'eliminar-empleado'),
]
