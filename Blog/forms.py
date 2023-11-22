from django import forms
from .models import Comentario

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['autor', 'email', 'cuerpo']
        
class BusquedaForm(forms.Form):
    consulta = forms.CharField()
    