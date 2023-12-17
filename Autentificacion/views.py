from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserCreationWithEmailForm, UserEditForm, ProfileEditForm
from django.contrib.auth.decorators import login_required

# Para crear la clase que nos servirá para registrar un nuevo usuario
from django.views.generic import View

# from django.contrib.auth.forms import UserCreationForm

from .models import Profile

# Para mostrar mensajes
from django.contrib import messages


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
            # Crea el objeto Profile
            Profile.objects.create(user=new_user)
            login(request, new_user, backend='django.contrib.auth.backends.ModelBackend')
            # una vez logueado hacemos la redirección a la pagina principal
            return redirect("Proyecto_web_app:home")
        return render(
            request, "Autentificacion/registro.html", {"user_form": user_form}
        )
    
@login_required
def dashboard(request):
    return render(request, "Autentificacion/dashboard.html")


# @login_required
# def edit(request):
#     if request.method == "POST":
#         user_form = UserEditForm(instance=request.user, data=request.POST)
#         profile_form = ProfileEditForm(
#             instance=request.user.profile, data=request.POST, files=request.FILES
#         )
#         if user_form.is_valid() and profile_form.is_valid():
#             user_form.save()
#             profile_form.save()
#             messages.success(request, 'Actualización del Perfil realizada correctamente.')
#         else:
#             messages.error(request, 'Error actualizando tu Perfil.')
#     else:
#         user_form = UserEditForm(instance=request.user)
#         profile_form = ProfileEditForm(instance=request.user.profile)
#     return render(
#         request,
#         "Autentificacion/edit.html",
#         {"user_form": user_form, "profile_form": profile_form},
#     )

@login_required
def edit(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = None
        
    if request.method == "POST":
        user_form = UserEditForm(instance=request.user, data=request.POST)
        if profile:
            profile_form = ProfileEditForm(
                instance=profile, data=request.POST, files=request.FILES
            )
        else:
            # Si el perfil no existe, crea uno nuevo
            profile_form = ProfileEditForm(
                data=request.POST, files=request.FILES
            )
            
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            if profile:
                profile_form.save()
            else:
                new_profile = profile_form.save(commit=False)
                new_profile.user = request.user
                new_profile.save()
            messages.success(request, 'Actualización del Perfil realizada correctamente.')
        else:
            messages.error(request, 'Error actualizando tu Perfil.')
    else:
        user_form = UserEditForm(instance=request.user)
        if profile:
            profile_form = ProfileEditForm(instance=profile)
        else:
            profile_form = ProfileEditForm()
    return render(
        request,
        "Autentificacion/edit.html",
        {"user_form": user_form, "profile_form": profile_form},
    )

