from django.shortcuts import render
from .forms import TableroForm
import random
from .buscaminas import Casilla, Tablero

def crear_tablero(request):
    tablero = None

    if request.method == 'POST':
        form = TableroForm(request.POST)
        if form.is_valid():
            filas = form.cleaned_data['filas']
            columnas = form.cleaned_data['columnas']
            minas = form.cleaned_data['minas']
            
            tablero = Tablero(filas, columnas, minas)
            tablero.colocar_minas()
            tablero.actualizar_minas_adyacentes(filas, columnas)

            tablero_tabla = []  
        for fila in tablero.casillas:
            fila_tablero = []
            for casilla in fila:
                if casilla.tiene_mina:
                    fila_tablero.append('X')
                else:
                    fila_tablero.append(casilla.minas_adyacentes)
            tablero_tabla.append(fila_tablero)

            return render(request, 'crear_tablero.html', {'tablero': tablero})
            #tablero = [['' for _ in range(columnas)] for _ in range(filas)]
            return
    else:
        form = TableroForm()

    return render(request, 'crear_tablero.html', {'form': form, 'tablero': tablero})

def indexer(request):
    return render(request, 'index.html')
