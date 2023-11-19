from django.shortcuts import render
from .forms import TableroForm
from .buscaminas import Tablero

def crear_tablero(request):
    tablero = None

    if request.method == 'POST':
        form = TableroForm(request.POST)
        if form.is_valid():
            filas = form.cleaned_data['filas']
            columnas = form.cleaned_data['columnas']
            minas = form.cleaned_data['minas']

            tablero = Tablero(filas, columnas, minas)
    else:
        form = TableroForm()

    return render(request, 'crear_tablero.html', {'form': form, 'tablero': tablero})

def indexer(request):
    return render(request, 'index.html')
