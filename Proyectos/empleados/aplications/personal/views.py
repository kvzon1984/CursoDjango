from django.db.models import fields
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView
)
from .models import Empleados


# Create your views here.


class InicioView(TemplateView):
    template_name = "inicio.html"


class AllEmpleadosListView(ListView):
    # 1.- Lista todos los empleados de la empresa
    template_name = 'personal/listempleados.html'
    ordering = 'id'
    paginate_by = 4

    def get_queryset(self):
        palabraclave = self.request.GET.get("buscador", '')
        lista = Empleados.objects.filter(
            full_name__icontains=palabraclave
        )
        return lista




class AreaEmpleadosListView(ListView):
    # 2.- Listar todos los empleados que pertenecen a un area de la empresa
    template_name = 'personal/listarempleadosarea.html'
    conctext_object_name= 'empleados'
  

    def get_queryset(self):
        area = self.kwargs['codigo']#Esta linea de codigo recupera los argumentos pasados por URL con la variable codigo
        lista = Empleados.objects.filter(
            departamento_id__short_name=area
        )
          
        return lista

# 3.- Listar empleados por trabajo



class ListEmpleadoKeyWord(ListView):
   # 4.- Listar empleados por plabra clave
    template_name = 'personal/ListaPalabraClave.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        palabraclave = self.request.GET.get("buscador", '')
        lista = Empleados.objects.filter(
            first_name=palabraclave
        )
        return lista

class ListHabilidadEmpleado(ListView):
    # 4.- Listar habilidades de un empleado

    template_name = 'personal/halibidadEmpleado.html'
    context_object_name = 'habilidades'

    def get_queryset(self):
        buscarNombre = self.request.GET.get("buscanombre", '')
        nombre = buscarNombre

        empleado = Empleados.objects.get(
            first_name=nombre
        )

        return empleado.habilidades.all()


class VerEmpleadoDetailView(DetailView):
    model = Empleados
    template_name = "personal/verempleado.html"

    def get_context_data(self, **kwargs):
        context = super(VerEmpleadoDetailView, self).get_context_data(**kwargs)
        # context["titulo"] = 'Empleado del mes'
        return context


class EmpleadoCreateView(CreateView):
    model = Empleados
    template_name = "personal/create.html"
    # fields=[
    #     'first_name',
    #     'last_name',
    #     'job'
    # ]
    fields = ['first_name', 'last_name', 'job',
              'departamento_id', 'habilidades', 'hoja_vida']
    success_url = reverse_lazy('personal_all:listarEmpleado')

    def form_valid(self, form):
        """Logica para realizar el full_name"""

        empleado = form.save(commit=False)
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()
        
        return super(EmpleadoCreateView, self).form_valid(form)



class EmpleadoUpdateView(UpdateView):
    model = Empleados
    template_name = "personal/update.html"

    fields = [
        'first_name', 
        'last_name', 
        'job',
        'departamento_id', 
        'habilidades', 
    ]
    success_url = reverse_lazy('personal_all:listarEmpleado')

    def post(self, request, *args, **kwargs):
        empleado = request.POST
        
        empleado['full_name'] = empleado['first_name'] + \
            ' ' + empleado['last_name']

        print('****************************' + empleado['full_name'])
        empleado['full_name'].save()
        return super(EmpleadoUpdateView, self).post(request, *args, **kwargs)


class EmpleadoDeleteView(DeleteView):
    model = Empleados
    template_name = "personal/delete.html"
    success_url = reverse_lazy('personal_all:listarEmpleado')


    
       
