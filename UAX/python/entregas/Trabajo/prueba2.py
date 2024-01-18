SIMBOLO_EMPEZAR = 'E'
SIMBOLO_MURO = '#'
SIMBOLO_MINA = '*'
SIMBOLO_TUNEL = 'o'
SIMBOLO_VACIO = '-'
SIMBOLO_SALIDA = 'S'

class Probabilidad:
    def _init_(self):
        self.pos_x = self.pos_inicial_x
        self.pos_y = self.pos_inicial_y
        
    def establecer_pos_inicial(self, lista):
        for i in range(len(lista)):
            for j in range(len(lista[i])):
                if lista[i][j] == SIMBOLO_EMPEZAR:
                    self.pos_inicial_x = i
                    self.pos_inicial_y = j
    
    def establecer_casillas_salida(self, lista):
        self.coordenadas_x_salidas = []
        self.coordenadas_y_salidas = []
        for i in range(len(lista)):
            for j in range(len(lista[i])):
                if lista[i][j] == SIMBOLO_SALIDA:
                    self.coordenadas_x_salidas.append(i)
                    self.coordenadas_y_salidas.append(j)
                    
    def establecer_casillas_tuneles(self):
        self.coordenadas_x_tuneles = []
        self.coordenadas_y_tuneles = []
        
        
    def mover_arriba(self):
        if self.pos_y != 0:
            self.w = self.pos_y - 1 
        
    def mover_abajo(self, lista):
        if self.pos_y != len(lista):
            self.s = self.pos_y + 1
        
    def mover_derecha(self, lista):
        if self.pos_x != len(lista[self.pos_y]):
            self.d = self.pos_x + 1    
        
    def mover_izquierda(self):
        if self.pos_y != 0:
            self.a = self.pos_x - 1
            
    def movimiento_aleatorio(self):
        self.num_aleatorio = random.randint(1,4)
        if self.num_aleatorio == 1:
            self.mover_arriba()
        elif self.num_aleatorio == 2:
            self.mover_abajo()
        elif self.num_aleatorio == 3:
            self.mover_derecha()
        elif self.num_aleatorio == 4:
            self.mover_izquierda()
            
    def algo(self):
        intentos = 1
        for i in range(len(self.coordenadas_x_salidas)):
            vivo = True
            while vivo:
                self.movimiento_aleatorio()
                if (self.pos_x, self.pos_y) == (self.coordenadas_x_salidas[i],self.coordenadas_y_salidas[i]):
                    vivo = False
                intentos += 1
        return print(intentos)
                
        

class Tablero(Probabilidad):
    def _init_(self):
        self.tabla = []
        
    def pregunta_fila_columna_tunel(self):
        while True:
            input1 = input("Pon el número de filas, columnas y túneles que va a tener el laberinto. \n: ").rstrip().split()
            try:
                self.filas = int(input1[0])
                self.columnas = int(input1[1])
                self.tuneles = int(input1[2])
                if ((self.filas, self.columnas >= 1) and (self.filas, self.columnas < 20) and (self.filas * self.columnas  > 2 * self.tuneles)):
                    return self.filas, self.columnas, self.tuneles
                else:
                    print("Los números no son válidos.")
            except:
                print("La cadena no es válida.")
                
    def crear_tablero(self):
        for i in range(self.filas):
            row = input(": ").rstrip().split()
            while len(row) != self.columnas:
                print("La dimensión de la fila no es la correcta")
                row = input(": ").rstrip().split()
            self.tabla.append(row)
        return self.tabla
                
    def preguntar_tunel(self):
        self.lista_para_tuneles = []
        for _ in range(self.tuneles):
            self.i1 = input(": ").rstrip()
            while ((self.i1 != int(self.i1)) and (self.i1 < 1)):
                print("No vale")
                self.i1 = input(": ").rstrip()
                
            super().coordenadas_x_tuneles.append(self.i1)
                
            self.j1 = input(": ").rstrip()
            while ((self.j1 != int(self.j1)) and (self.j1 < 1)):
                print("No vale")
                self.j1 = input(": ").rstrip()
                
            super().coordenadas_y_tuneles.append(self.j1)
            
            self.i2 = input(": ").rstrip()
            while ((self.i2 != int(self.i2)) and (self.i2 > self.filas)):
                print("No vale")
                self.i2 = input(": ").rstrip()
                
            super().coordenadas_x_tuneles.append(self.i2)
            
            self.j2 = input(": ").rstrip()
            while ((self.j2 != int(self.j2)) and (self.j2 > self.filas)):
                print("No vale")
                self.j2 = input(": ").rstrip()
                
            super().coordenadas_y_tuneles.append(self.j2)       
            
            
    def crear_tunel_en_tabla(self):
        cord_1 = self.lista_para_tuneles[0]
        cord_2 = self.lista_para_tuneles[1]
        self.tabla[cord_1][cord_2] = SIMBOLO_TUNEL
        

       
def imprimir_tablero(tablero):
    for i in (range(len(tablero))):
        for j in (range(len(tablero[i]))):
            print(tablero[i][j], end=' ')
        print()
        
        
        
        
        
            
tabla = Tablero()
tabla.pregunta_fila_columna_tunel()
tabla.establecer_casillas_tuneles()
tabla.preguntar_tunel()
tablero = tabla.crear_tablero()
tabla.establecer_pos_inicial(tablero)
tabla.establecer_casillas_salida(tablero)
tabla.algo()
imprimir_tablero(tabla.crear_tablero())