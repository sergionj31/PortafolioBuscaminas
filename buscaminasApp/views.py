from django.shortcuts import render
from .forms import TableroForm
import random

def crear_tablero(request):
    tablero = None

    if request.method == 'POST':
        form = TableroForm(request.POST)
        if form.is_valid():
            filas = form.cleaned_data['filas']
            columnas = form.cleaned_data['columnas']
            
            #return render(request, 'muestra_tablero.html', {'filas':filas,'columnas':columnas})
            tablero = [['' for _ in range(columnas)] for _ in range(filas)]

    else:
        form = TableroForm()

    return render(request, 'crear_tablero.html', {'form': form, 'tablero': tablero})

def indexer(request):
    return render(request, 'index.html')
