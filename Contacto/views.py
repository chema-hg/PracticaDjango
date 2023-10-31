from django.shortcuts import render, redirect

from .forms import FormularioContacto

from django.urls import reverse

# Para que el correo electrónico funcione en un hilo aparte.
import threading

# Para enviar el correo electronico
from django.core.mail import send_mail, EmailMessage
from django.conf import settings


def enviar_email_en_hilo(correo):
    """Enviará el email en un hilo aparte para que no se bloquee el programa."""
    correo.send()


# Create your views here.


def contacto(request):
    formulario_contacto = FormularioContacto()

    # Si se ha hecho "POST" rescata la información del diccionario enviado.
    if request.method == "POST":
        # El método post devuelve un diccionario con los datos del formulario
        formulario_contacto = FormularioContacto(data=request.POST)
        # Si el formulario de contacto es válido, se han rellenado los campos obligatorios
        # y los campos están bien definidos.
        if formulario_contacto.is_valid():
            datos = formulario_contacto.cleaned_data
            nombre = datos.get("nombre")
            email = datos.get("email")
            contenido = datos.get("contenido")
            # Sin usar los datos validados, los cogemos del POST directamente.
            # nombre = request.POST.get("nombre")
            # email = request.POST.get("email")
            # contenido = request.POST.get("contenido")

            # Para enviar el correo electrónico
            email_from = settings.EMAIL_HOST_USER
            email_to = settings.EMAIL_DESTINATION

            # Esta sería una forma de enviarlo que ya vimos en el capitulo anterior.
            # send_mail(
            # f'Mensaje de {nombre}',
            # f'{contenido} \nemail: {email}',
            # email_from,
            # [email_to],
            # )

            # Para enviar el correo electrónico de otra forma
            correo = EmailMessage(
                "Mensaje desde APP Django",
                f"El usuario {nombre} con la direccion {email} escribe lo siguiente:\n\n{contenido}",
                email_from,
                [email_to],
                reply_to=[email],  # Para responder al correo del que nos escribe.
            )
            try:            
                # Enviar el correo en un hilo aparte
                thread = threading.Thread(target=enviar_email_en_hilo, args=(correo,))
                thread.start()
                url_exito = reverse("Contacto:contacto") + "?valido"
                return redirect(url_exito)
            except:
                url_exito = reverse("Contacto:contacto") + "?novalido"
                return redirect(url_exito)
            # en get se pasan los parametros por la url usando ?

    return render(request, "Contacto/contacto.html", {"form": formulario_contacto})
