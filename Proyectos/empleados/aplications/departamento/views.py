from django.shortcuts import render


from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from aplications.personal.models import Empleados
from .models import Departamento
from .froms import NewDepartamentoForm

# Create your views here.



class ListaDepartamentoListView(ListView):
    model = Departamento
    template_name = "departamento/listaDepartamento.html"
    context_object_name = 'departamentos'



class NewDepartamentoView(FormView):
    template_name = 'departamento/new_departamento.html'
    form_class = NewDepartamentoForm
    success_url = '/'

    def form_valid(self, form):

        depa = Departamento(

            name=form.cleaned_data['departamento'],
            short_name=form.cleaned_data['departamentoNombreCorto'],

        )

        depa.save()

        name= form.cleaned_data['nombre']
        apellido = form.cleaned_data['apellidos']
        Empleados.objects.create(
            first_name = name,
            last_name = apellido,
            job = '1',
            departamento_id = depa
        )

        return super(NewDepartamentoView, self).form_valid(form)
