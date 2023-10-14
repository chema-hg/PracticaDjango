from django.shortcuts import render, HttpResponse

from Servicios.models import Servicio

# Create your views here.

def home(request):
    return render(request, 'Proyecto_web_app/inicio.html')

def servicios(request):
    servicios = Servicio.objects.all()
    return render(request, 'Proyecto_web_app/servicios.html', {'servicios': servicios})

def tienda(request):
    return render(request, 'Proyecto_web_app/tienda.html')

def blog(request):
    return render(request, 'Proyecto_web_app/blog.html')

def contacto(request):
    return render(request, 'Proyecto_web_app/contacto.html')