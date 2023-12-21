from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request, 'Proyecto_web_app/inicio.html')


