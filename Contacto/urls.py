from django.urls import path
# load views of these applications.
from . import views

app_name = 'Contacto'

urlpatterns = [
    path('', views.contacto, name='contacto'),
]