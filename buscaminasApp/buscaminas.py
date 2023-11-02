from .forms import TableroForm

class tablero:
    num_filas = 0
    num_columnas = 0
    num_minas = 0

def __init__(self, num_filas, num_columnas, num_minas):
    self.num_filas = num_filas
    self.num_columnas = num_columnas
    self.num_minas = num_minas

def 

class casilla:
    fila = 0
    columna = 0
    es_mina = False
    adyacentes = 0

def __init__(self, fila, columna, es_mina, adyacente):
    self.fila = fila
    self.columna = columna
    self.es_mina = es_mina
    self.adyacente = adyacente