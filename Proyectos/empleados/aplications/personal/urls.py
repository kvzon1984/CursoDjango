from re import I
from django.contrib import admin
from django.urls import path
from . import views

app_name = 'personal_all'

urlpatterns = [
    path('', 
        views.InicioView.as_view(),
        name='inicio'),
    path('listarempleados/', 
        views.AllEmpleadosListView.as_view(),
        name='listarEmpleado'),
    path('listarempleadosarea/<codigo>', 
        views.AreaEmpleadosListView.as_view(),
        name='listaEmpleadosArea'),
    path('buscarempleado/',
        views.ListEmpleadoKeyWord.as_view(),
        name='buscarEmpleado'),
    path('habilidadempleado/', 
        views.ListHabilidadEmpleado.as_view(),
        name='habilidadEmpleado'),
    path('verempleado/<pk>', 
        views.VerEmpleadoDetailView.as_view(), 
        name='detalleEmpleado'),
    path('create/', 
        views.EmpleadoCreateView.as_view(),
        name='createEmpleado'),
    path('update/<pk>', 
        views.EmpleadoUpdateView.as_view(), 
        name='update'),
    path('delete/<pk>', 
        views.EmpleadoDeleteView.as_view(), 
        name='delete'),
]