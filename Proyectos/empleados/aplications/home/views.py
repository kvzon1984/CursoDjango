from django.db import models
from django.shortcuts import render
from django.views.generic import (
    TemplateView, 
    ListView,
    CreateView)

from aplications.home.forms import PruebaForm
from .models import Prueba

# Create your views here.
class PruebaView(TemplateView):
    template_name = 'home/prueba.html'


class ResumenFoundationView(TemplateView):
    template_name = 'home/resumen_foundation.html'



class PruebaListView(ListView):
    template_name = "home/lista.html"
    context_object_name = 'listaNumeros'
    queryset = ['1', '10', '20', '30', '40']
    

class listar_prueba(ListView):
    template_name = "home/listar_prueba.html"
    model = Prueba
    context_object_name = 'lista'

class PruebaCreateView(CreateView):
    model = Prueba
    template_name = "home/add.html"
    form_class = PruebaForm
    success_url = "/"
    