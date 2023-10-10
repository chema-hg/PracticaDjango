from django.urls import path
from . import views

app_name  = 'Proyecto_web_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('servicios/', views.servicios, name='servicios'),
    path('tienda/', views.tienda, name='tienda'),
    path('blog/', views.blog, name='blog'),
    path('contacto/', views.contacto, name='contacto'),

]