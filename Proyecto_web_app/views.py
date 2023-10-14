from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request, 'Proyecto_web_app/inicio.html')

def tienda(request):
    return render(request, 'Proyecto_web_app/tienda.html')

def blog(request):
    return render(request, 'Proyecto_web_app/blog.html')

def contacto(request):
    return render(request, 'Proyecto_web_app/contacto.html')