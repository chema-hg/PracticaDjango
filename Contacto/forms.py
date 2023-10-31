from django import forms


class FormularioContacto(forms.Form):
    # Especificamos los campos del formulario
    nombre = forms.CharField(label="Nombre", max_length=50)
    email = forms.EmailField(label="Email", max_length=50)
    contenido = forms.CharField(
        label="Contenido",
        max_length=400,
        widget=forms.Textarea(attrs={"cols": 45, "rows": 5}),
    )
