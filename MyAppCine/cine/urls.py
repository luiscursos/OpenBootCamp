from . import views # Importamos las views de nuestro modulo cine
from django.urls import path

urlpatterns=[
    path('', views.index,name='index')
]