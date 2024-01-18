### LABERINTO ###

import random


SIMBOLO_EMPEZAR = 'E'
SIMBOLO_MURO = '#'
SIMBOLO_MINA = '*'
SIMBOLO_TUNEL = 'o'
SIMBOLO_VACIO = '-'
SIMBOLO_SALIDA = 'S'

        

'''
La clase Tablero permite tanto crear, como recorrer, como asignar la probabilidad de que que salga del laberinto 
con éxito. 
La lógica para el algoritmo de cálculo de la probabilidad ha sido la recursividad, puesto que se realiza un número elevado de 
intentos y se contabilizan aquellos intentos en los que llega a la salida.
'''

class Tablero:
    def __init__(self, intentos_totales: int): # Se le asigna un número de intentos para que el cálculo sea con un número elevado de intentos
        self.tabla = []
        self.pos_x = 0
        self.pos_y = 0
        self.intentos_totales = intentos_totales
        self.intentos_validos = 0
        self.intentos_fallidos = 0
        self.probabilidad = self.intentos_validos / self.intentos_totales
        
        
    def pregunta_fila_columna_tunel(self):  # Este método permite conocer el número de filas, columnas y túneles que hay en el laberinto
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
                
    def crear_tablero(self):  # Partiendo de una lista vacia, self.lista, se añaden los distintos símbolos para rellenar completamente el laberinto
        print("MURO: '#'  MINA: '*'  VACIO: '-'  ENTRADA: 'E'  SALIDA: 'S'")
        for i in range(self.filas):
            row = input(f"Fila {i}: ").rstrip() #.split()
            while len(row) != self.columnas:
                print("La dimensión de la fila no es la correcta")
                imprimir_tablero(self.tabla)
                row = input(f"Fila {i}:").rstrip() #.split()
            self.tabla.append(row)
        return self.tabla
                
    def preguntar_tunel(self):  # En el caso de que haya túneles, se preguntarán las coordenadas del túnel. Cada túnel está asociado a otro túnel de manera única, para esto hemos utilizado un diccionario
        self.coordenadas_tunel = {}
        if self.tuneles == 0:
            return "0 tuneles"
        else:
            for _ in range(self.tuneles):
                i1 = input("La fila del tunel (La primera fila es el 0). \n: ").rstrip()
                try:
                    i1 = int(i1)
                    if 0 <= i1 <= self.filas:
                        pass
                    else:
                        print("Ese número no vale")
                        continue
                except:
                    print("Formato no válido.")
                    continue
                    
                j1 = input("La columna del tunel (La primera columna es el 0). \n: ").rstrip()
                try:
                    j1 = int(j1)
                    if 0 <= j1 <= self.columnas:
                        pass
                    else:
                        print("Ese número no vale")
                        continue
                except:
                    print("Formato no válido")
                    continue
                    
                i2 = input(f"La fila del tunel (la primera fila es el 0) que está conectado al tunel ({i1},{j1}). \n: ").rstrip()
                try:
                    i2 = int(i2)
                    if 0 <= i2 <= self.filas:
                        pass
                    else:
                        print("Ese número no vale")
                        continue
                except:
                    print("Formato no válido.")
                    continue
                            
                j2 = input(f"La columna del tunel (La primera columna es el 0) que está conectada al tunel ({i1},{j1}). \n: ").rstrip()
                try:
                    j2 = int(j2)
                    if 0 <= j2 <= self.columnas:
                        pass                    
                    else:
                        print("Ese número no vale")
                        continue
                except:
                    print("Formato no válido")
                    continue
                    
                self.coordenadas_tunel[(i1, j1)] = (i2, j2)
                self.coordenadas_tunel[(i2, j2)] = (i1, j1)
            return "Tuneles registrados correctamente", self.coordenadas_tunel
                           
    def establecer_pos_inicial(self):  # Como la posición inicial no siempre es (0,0), esta función permite buscar el símbolo "E", desde el que partirá la rana para recorrer el laberinto
        for i in range(self.filas):
            for j in range(self.columnas):
                if self.tabla[i][j] == SIMBOLO_EMPEZAR:
                    self.pos_x = i
                    self.pos_y = j  
        return self.pos_x, self.pos_y
    
    def dibujar_tunel_en_tabla(self):  # Este método añade al tablero el icono del túnel a partir de las coordenadas guardadas en el diccionario anteriormente creado
        for i in range(self.filas):
            for j in range(self.columnas):
                if (i, j) in self.coordenadas_tunel:
                    self.tabla[i] = self.tabla[i][:j] + SIMBOLO_TUNEL + self.tabla[i][j+1:]            
        imprimir_tablero(self.tabla)
        return self.coordenadas_tunel
    

    def config(self):  # Este método añade los anteriores los cuales permiten que el laberinto esté configurado y listo para poder calcular la probabilidad sobre él
        self.pregunta_fila_columna_tunel()
        self.crear_tablero()
        self.establecer_pos_inicial()
        self.preguntar_tunel()
        self.dibujar_tunel_en_tabla()


    
    ''' ARRIBA '''
    ###
    def comprobar_mover_arriba(self): # Verifica que se pueda mover para arriba si no hay muro o está arriba del todo
        if self.pos_x != 0 and (self.tabla[self.pos_x - 1][self.pos_y] != SIMBOLO_MURO):
            return True # Se puede mover
        else:
            return False # No se puede mover
    
    def mover_arriba(self):  # Movimiento hacia arriba
        self.pos_x = self.pos_x - 1
    ###    
    
    
    ''' ABAJO '''
    ###         
    def comprobar_mover_abajo(self): # Verifica si se puede mover hacia abajo si no hay muro o está abajo del todo  
        if self.pos_x != (self.filas - 1) and (self.tabla[self.pos_x + 1][self.pos_y] != SIMBOLO_MURO):
            return True  # Se puede mover
        else:
            return False  # No se puede mover
              
    def mover_abajo(self):  # Movimiento hacia abajo
        self.pos_x = self.pos_x + 1
    ###
       
       
    ''' DERECHA '''   
    ###
    def comprobar_mover_derecha(self): # Verifica que se pueda mover a la derecha si no hay muro o si no está a la derecha del todo
        if self.pos_y != (self.columnas - 1) and (self.tabla[self.pos_x][self.pos_y + 1] != SIMBOLO_MURO):
            return True  # Se puede mover
        else:
            return False  # No se puede mover
    
    def mover_derecha(self): # Movimiento a la derecha 
        self.pos_y = self.pos_y + 1 
    ###
     
     
    ''' IZQUIERDA ''' 
    ###    
    def comprobar_mover_izquierda(self): # Comprueba si se puede mover a la izquierda si no hay muro o si no está a la izquierda del todo
        if (self.pos_y != 0) and (self.tabla[self.pos_x][self.pos_y - 1] != SIMBOLO_MURO):
            return True  # Se puede mover
        else:
            return False   # No se puede mover
        
    def mover_izquierda(self): # Movimiento a la izquierda 
        self.pos_y = self.pos_y - 1
    ###
    
    
    ''' TUNEL '''
    ###
    def comprobar_tunel(self):  # En el caso de que se haya movido, una vez está en la nueva casilla, comprueba si está en un túnel
        if (self.pos_x, self.pos_y) in self.coordenadas_tunel:
            return True # Está encima de un túnel
   
    def mover_si_tunel(self):  # Si está en un túnel, su posición cambiará y será la salida del túnel
        posicion = self.coordenadas_tunel[(self.pos_x, self.pos_y)] # Esto permite buscar el valor en el diccionario donde se guardan las coordenadas
        self.pos_x = posicion[0]
        self.pos_y = posicion[1]
        return (self.pos_x, self.pos_y), "Ha pasado el tunel"
    ###
    
    
    ''' MINAS '''
    ###
    def encontrar_minas(self): # Esta función comprueba si estás encima de una mina 
        if self.tabla[self.pos_x][self.pos_y] == SIMBOLO_MINA:
            return True  # Estás encima de una mina
    ###    
    
    ''' SALIDA '''
    ###    
    def encontrar_salida(self):   # Comprueba si estás en una salida
        if self.tabla[self.pos_x][self.pos_y] == SIMBOLO_SALIDA:
            return True   # Estás en una salida
    ###
           
       
    def comprobaciones_wasd(self, num_aleatorio):  # Este método comprueba, en función del número aleatorio, que movimiento le corresponde en cada caso. Si se puede mover en la dirección que le ha tocado, se moverá. En caso de que no se pueda mover no se moverá, y después utilizará otro número aleatorio para verificar
        if (num_aleatorio == 1):  # Mover hacia arriba
            if (self.comprobar_mover_arriba() == True):
                self.mover_arriba()
                return True
            else:
                return False
        elif (num_aleatorio == 2): # Mover hacia abajo
            if (self.comprobar_mover_abajo() == True):
                self.mover_abajo()
                return True
            else:
                return False
        elif (num_aleatorio == 3):  # Mover hacia la izquierda
            if (self.comprobar_mover_izquierda() == True):
                self.mover_izquierda()
                return True
            else:
                return False
        elif (num_aleatorio == 4):  # Mover a la derecha
            if (self.comprobar_mover_derecha() == True):
                self.mover_derecha()
                return True
            else:
                return False
        elif (self.comprobar_mover_abajo() == False) and (self.comprobar_mover_arriba() == False) and (self.comprobar_mover_derecha() == False) and (self.comprobar_mover_izquierda() == False):
            return False
        
        
    def comprobaciones_minas_tunel_salida(self):  # En el caso de que se haya movido, este método comprobará si se encuentra encima de una mina, un túnel, o una salida, y hará la lógica correspondiente a cada caso
        if self.encontrar_minas() == True:
            self.intentos_fallidos += 1
            return False 
        elif self.comprobar_tunel() == True:
            self.mover_si_tunel()
            return True        
        elif self.encontrar_salida() == True:
            self.intentos_validos += 1
            return False
        return True
    '''
    Este método devuelve un valor booleano que se almacenará en la variable del siguiente método "vivo", la cual mientras 
    sea verdadera seguirá haciendo comprobaciones. En el caso de que sea False, significa que dejará de estar vivo y comenzará 
    otro bucle. 
    Por defecto siempre devuelve un True
    '''


    '''
    Realizará el número de intentos que se establezca. El estado de la rana se almacena en la variable "vivo" la cual empezará siendo True;
    mientras que la rana siga viva y no supere el número máximo de iteraciones hará los movimientos. 
    1) Primero se obtendrá un número aleatorioentre el 1 y el 4, se utilizará el método self.comprobar_wasd() 
    que permitirá comprobar los movimientos y hacerlos en caso de que se pueda. 
    2) Si se ha conseguido mover, irá a la siguiente comprobación utilizando el método self.comprobaciones_minas_tunel_salida() que 
    realizará la lógica correspondiente a dicho método.
    Para elaborar este método hemos tenido en cuenta distintos fallos que pueden ocurrir.
    - En el caso de que se quede atrapado, no se podrá mover, por lo que hará un número infinito de comprobaciones de movimiento. Para
    solucionarlo hemos limitado el número máximo de iteraciones; en el caso de que se supere este número de iteraciones, irá al
    intento.
    
    '''
    def asignar_probabilidad(self):
        for _ in range(self.intentos_totales):
            vivo = True
            iteraciones = 0
            iteraciones_maximas = 10 * self.filas * self.columnas

            while vivo and iteraciones < iteraciones_maximas:
                direccion_aleatoria = random.randint(1, 4)
                validar_movimiento = self.comprobaciones_wasd(direccion_aleatoria)

                if validar_movimiento:
                    vivo = self.comprobaciones_minas_tunel_salida()
                    if not vivo:
                        self.establecer_pos_inicial()
                else:
                    vivo = True

                iteraciones += 1
                    
        return print(f"La probabilidad de escapar es de: {self.intentos_validos / self.intentos_totales}")
        
            


def imprimir_tablero(tablero):  # Esta función permite mostrar el tablero por pantalla
    for i in (range(len(tablero))):
        for j in (range(len(tablero[i]))):
            print(tablero[i][j], end=' ')
        print()
        

if __name__ == "__main__":
    tablero = Tablero(1000)
    tablero.config()
    tablero.asignar_probabilidad()