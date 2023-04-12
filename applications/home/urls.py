from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.Index.as_view()),
    path('lista/', views.Prueba_listview.as_view()),
    path('lista-prueba/', views.ModeloPruebaListView.as_view()),
    path('add-createview/', views.PruebaCreateView.as_view(), name = 'prueba_add'),
    path('resume-foundation/', views.ResumeFoundationView.as_view(), name = 'resume_foundation'),
]
   