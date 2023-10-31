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
            minas = form.cleaned_data['minas']

            arrayMinas = []

            for mina in range(minas):
                randomFila = round(random.random()*filas)
                randomColumna = round(random.random()*columnas)
                mina = ({randomFila},{randomColumna})
                arrayMinas.append(mina)

            #return render(request, 'muestra_tablero.html', {'filas':filas,'columnas':columnas})
            tablero = [['' for _ in range(columnas)] for _ in range(filas)]

            for row in range(tablero):
                for column in range(tablero):
                    for coordMina in range(minas):
                        if (row == coorMina[0] and column == coorMina[1]):
                            tablero[row][column] = "mina"

                

    else:
        form = TableroForm()

    return render(request, 'crear_tablero.html', {'form': form, 'tablero': tablero})

def indexer(request):
    return render(request, 'index.html')
