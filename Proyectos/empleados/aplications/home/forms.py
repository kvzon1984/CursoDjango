from django import forms
from django.forms import widgets
from django.forms.widgets import Widget
from .models import Prueba




class PruebaForm(forms.ModelForm):
    """Form definition for Prueba."""

    class Meta:
        """Meta definition for Pruebaform."""

        model = Prueba
        fields = (
            'titulo',
            'subtitulo',
            'cantidad'
        )

        widgets = {
            'titulo': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese Titulo',
                    'class' : 'titulo prueba'
                }
            )
        }

    def clean_cantidad(self):
        cantidad = self.cleaned_data.get('cantidad')

        if cantidad < 10:
            raise forms.ValidationError('Ingrese un munero mayor a 10')
    
    
         # TODO Validation
    
        return cantidad
