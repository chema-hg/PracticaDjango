from django import forms

class CuponFormulario(forms.Form):
    codigo = forms.CharField(max_length=50)