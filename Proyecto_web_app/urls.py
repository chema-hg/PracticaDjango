from django.urls import path
from . import views

app_name  = 'Proyecto_web_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('tienda/', views.tienda, name='tienda'),
    #path('contacto/', views.contacto, name='contacto'),
]