from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserCreationWithEmailForm

# Para crear la clase que nos servirá para registrar un nuevo usuario
from django.views.generic import View
# from django.contrib.auth.forms import UserCreationForm


def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request, username=cd["username"], password=cd["password"]
            )
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse("Autentificación realizada con éxito")
                else:
                    return HttpResponse("Cuenta desactivada")
            else:
                return HttpResponse("Inicio de sesión no válido")
    else:
        form = LoginForm()
        return render(request, "Autentificacion/login.html", {"form": form})

class registrar(View):
    
    def get(self, request):
        # creamos el formulario y se lo pasamos a la plantilla
        user_form = UserCreationWithEmailForm()
        return render(
            request, "Autentificacion/registro.html", {"user_form": user_form}
        )

    def post(self, request):
        user_form = UserCreationWithEmailForm(request.POST)
        # si el formulario es válido
        if user_form.is_valid():
            # Creamos un nuevo usuario y lo guardamos en la base de datos.
            new_user = user_form.save()
            # con .save() se guarda en la base de datos el hash de la contraseña y el usuario.
            # Al crear una cuenta si el registro
            # tiene exito el usuario se logea automáticamente y se redirecciona
            # a la pagina de inicio
            login(request, new_user)
            # una vez logueado hacemos la redirección a la pagina principal
            return redirect("Proyecto_web_app:home")
        return render(
            request, "Autentificacion/registro.html", {"user_form": user_form}
        )
