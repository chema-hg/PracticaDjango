from django.urls import path

from . import views

app_name = 'Servicios'

urlpatterns = [
    path('', views.servicios, name='servicios'),
]