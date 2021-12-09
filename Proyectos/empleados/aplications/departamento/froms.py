from django import forms
from django.forms import widgets

class NewDepartamentoForm(forms.Form):
    """NewDepartamentoForm definition."""
    nombre = forms.CharField(max_length=50)
    apellidos = forms.CharField(max_length=50)
    departamento = forms.CharField(max_length=50)
    departamentoNombreCorto = forms.CharField(max_length=20)

    # widgets = {
    #     'nombre' : forms.TextInput(
    #         attrs={
    #             'placeholder':'Nombre'

    #         }
    #     ),
    #     'apellidos': forms.TextInput(
    #         attrs={
    #             'placeholder': 'Apellidos'

    #         }
    #     ),
    #     'departamento': forms.TextInput(
    #         attrs={
    #             'placeholder': 'Nombre Departamento'

    #         }
    #     ),
    #     'departamentoNombreCorto': forms.TextInput(
    #         attrs={
    #             'placeholder': 'Nombre Corto Departamento'

    #         }
    #     ),
    # }
    # TODO: Define form fields here
