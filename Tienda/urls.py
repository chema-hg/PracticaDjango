from django.urls import path
# load views of these applications.
from . import views

app_name = 'Tienda'

urlpatterns = [
    path('', views.tienda, name='tienda'),
]