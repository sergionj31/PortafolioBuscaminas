from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexer, name='index'),
    path('crear_tablero', views.crear_tablero, name='crear_tablero')
]

