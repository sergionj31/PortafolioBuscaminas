from .forms import TableroForm
import random

class Casilla:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tiene_mina = False
        self.minas_adyacentes = 0

class Tablero:
    def __init__(self, filas, columnas, minas):
        self.filas = filas
        self.columnas = columnas
        self.minas = minas
        self.casillas = [[Casilla(x, y) for y in range(columnas)] for x in range(filas)]
        self.colocar_minas()
        self.actualizar_minas_adyacentes(filas, columnas)

    def colocar_minas(self):
        minas_colocadas = 0
        while minas_colocadas < self.minas:
            x, y = random.randint(0, self.filas - 1), random.randint(0, self.columnas - 1)
            if not self.casillas[x][y].tiene_mina:
                self.casillas[x][y].tiene_mina = True
                minas_colocadas += 1
                self.actualizar_minas_adyacentes(x, y)

    def actualizar_minas_adyacentes(self, x, y):
        for i in range(-1, 2):
            for j in range(-1, 2):
                nueva_x, nueva_y = x + i, y + j
                if 0 <= nueva_x < self.filas and 0 <= nueva_y < self.columnas:
                    self.casillas[nueva_x][nueva_y].minas_adyacentes += 1
