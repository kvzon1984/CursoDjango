from django.contrib import admin
from django.urls import path
from . import views


app_name = 'departamento'

urlpatterns = [
    path('new-departamento/', views.NewDepartamentoView.as_view(), name='new-departamento'),
    path('listaDepartamento/', views.ListaDepartamentoListView.as_view(),
         name='listaDepartamento'),
]
