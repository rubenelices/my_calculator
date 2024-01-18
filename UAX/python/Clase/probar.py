"""
Creo la clase tablero en la cual metero todo lo relacionado con
la ceación del tablero y la impresión de este
"""
class Tablero:
    def __init__(self):
        self.tablero = [
            ['♜', '♞', '♝', '♛', '♚', '♝', '♞', '♜'],
            ['♟', '♟', '♟', '♟', '♟', '♟', '♟', '♟'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['♙', '♙', '♙', '♙', '♙', '♙', '♙', '♙'],
            ['♖', '♘', '♗', '♕', '♔', '♗', '♘', '♖']
        ]
#Imprimo el tablero con un espacio entre cada fila para que quede mejor
    def imprimir_tablero(self):
        for fila in self.tablero:
            print(" ".join(fila))
        print()

"""
Creo la clase pieza para meter en ella todo lo relacionado con las caracteristicas 
de las piezas
"""
class Pieza:
    def __init__(self, color):
        self.color = color

    def mover(self, origen, destino, tablero):
        pass

"""
Creo la clase peón para meter en ella todo lo relacionado con el peon tanto
blanco como negro y como se podrá mover esta pieza, en este caso hay dos posibles
jugadas ya que el peón al principio de la partida puede hacer un movimiento especial
que es mover 2 casillas en vez de una
"""
class Peon(Pieza):
    def mover(self, origen, destino, tablero):
        fila_origen, columna_origen = origen
        fila_destino, columna_destino = destino

        if self.color == 'blanco':
            direccion = -1
        else:
            direccion = 1

        # Movimiento inicial de dos casillas
        if (fila_origen == 6 and self.color == 'blanco') or (fila_origen == 1 and self.color == 'negro'):
            if fila_destino == fila_origen + 2 * direccion and columna_destino == columna_origen and tablero[fila_destino][columna_destino] == ' ':
                tablero[fila_destino][columna_destino] = tablero[fila_origen][columna_origen]
                tablero[fila_origen][columna_origen] = ' '
                return True

        # Movimiento normal de una casilla
        if fila_destino == fila_origen + 1 * direccion and columna_destino == columna_origen and tablero[fila_destino][columna_destino] == ' ':
            tablero[fila_destino][columna_destino] = tablero[fila_origen][columna_origen]
            tablero[fila_origen][columna_origen] = ' '
            return True

        return False

"""
Creo la clase para la pieza torre en la cual metere todo lo relacionado con esta pieza
, en este caso defino la funcion moverse de tal manera que los unicos posibles movimientos
de la torre sean a lo largo de una columna o de una fila
"""
class Torre(Pieza):
    def mover(self, origen, destino, tablero):
        fila_origen, columna_origen = origen
        fila_destino, columna_destino = destino

        if fila_origen == fila_destino or columna_origen == columna_destino and tablero[fila_destino][columna_destino] == ' ':
            # Movimiento válido para una torre
            tablero[fila_destino][columna_destino] = tablero[fila_origen][columna_origen]
            tablero[fila_origen][columna_origen] = ' '
            return True

        return False

"""
Creo la clase caballo parameter en esta ttodo lo relacionado con esa pieza,
en este caso hago la función moverse que solo dejara al caballo moverse de 
tal forma que traze una "L"
"""
class Caballo(Pieza):
    def mover(self, origen, destino, tablero):
        fila_origen, columna_origen = origen
        fila_destino, columna_destino = destino

        movimientos_posibles = [
            (fila_origen + 2, columna_origen + 1),
            (fila_origen + 2, columna_origen - 1),
            (fila_origen - 2, columna_origen + 1),
            (fila_origen - 2, columna_origen - 1),
            (fila_origen + 1, columna_origen + 2),
            (fila_origen + 1, columna_origen - 2),
            (fila_origen - 1, columna_origen + 2),
            (fila_origen - 1, columna_origen - 2),
        ]

        if (fila_destino, columna_destino) in movimientos_posibles and tablero[fila_destino][columna_destino] == ' ':
            tablero[fila_destino][columna_destino] = tablero[fila_origen][columna_origen]
            tablero[fila_origen][columna_origen] = ' '
            return True

        return False

"""
la clase alfil hereda de la clase Pieza y en ella se implementa la función mover
con la lógica de movimiento del alfil para lo cual se calcula la diferencia entre las
coordenadas de cada eje y esta tiene que ser igual
La lógica esta simplificada ignorando la posibilidad de que haya piezas en medio y sin 
que se pueda realizar la acción de comer
"""
class Alfil(Pieza):
    def mover(self, origen, destino, tablero):
        fila_origen, columna_origen = origen
        fila_destino, columna_destino = destino

        if abs(fila_destino - fila_origen) == abs(columna_destino - columna_origen) and tablero[fila_destino][columna_destino] == ' ':
            # Movimiento válido para un alfil
            tablero[fila_destino][columna_destino] = tablero[fila_origen][columna_origen]
            tablero[fila_origen][columna_origen] = ' '
            return True

        return False


class Reina(Pieza):
    def mover(self, origen, destino, tablero):
        fila_origen, columna_origen = origen
        fila_destino, columna_destino = destino

        if (fila_origen == fila_destino or columna_origen == columna_destino or abs(fila_destino - fila_origen) == abs(columna_destino - columna_origen)) and tablero[fila_destino][columna_destino] == ' ':
            # Movimiento válido para una reina
            tablero[fila_destino][columna_destino] = tablero[fila_origen][columna_origen]
            tablero[fila_origen][columna_origen] = ' '
            return True

        return False

"""
Creo la clase rey para meter en ella todo lo relacionado con esta pieza,
en este caso hago que se pueda mover una casilla en todas las direcciones 
a casillas que no esten ocupadas
"""
class Rey(Pieza):
    def mover(self, origen, destino, tablero):
        fila_origen, columna_origen = origen
        fila_destino, columna_destino = destino

        if abs(fila_destino - fila_origen) <= 1 and abs(columna_destino - columna_origen) <= 1 and tablero[fila_destino][columna_destino] == ' ':
            # Movimiento válido para un rey
            tablero[fila_destino][columna_destino] = tablero[fila_origen][columna_origen]
            tablero[fila_origen][columna_origen] = ' '
            return True

        return False

"""
Creo la clase jugador para distinguir entre el jugador blanco y el negro
"""
class Jugador:
    def __init__(self, color):
        self.color = color

"""
Creo la clase juego que será con la que se inicie el juego determinando
un jugador blanco y uno negro y será la clase en la que se meterá todo lo relacionado
con la partida de ajedrez ya que se crean las preguntasque se va haciendo a los
jugadores en cada movimiento
"""
class Juego:
    def __init__(self):
        self.tablero = Tablero()
        self.jugador_blanco = Jugador('blanco')
        self.jugador_negro = Jugador('negro')

    def jugar(self):
        turno = 1
        while True:
            print(f"Turno {turno}")
            self.tablero.imprimir_tablero()

            jugador_actual = self.jugador_blanco if turno % 2 == 1 else self.jugador_negro
            origen = self.obtener_coordenadas("Elija la posición de la pieza que desea mover:")
            pieza = self.elegir_pieza(jugador_actual, origen, self.tablero.tablero)
            while  not pieza:
                origen = self.obtener_coordenadas("Elija la posición de la pieza que desea mover:")
                pieza = self.elegir_pieza(jugador_actual, origen, self.tablero.tablero)

            if pieza:
                
                movimiento_valido = False
                while not movimiento_valido:              
                    destino = self.obtener_coordenadas("Elija la posición a la que desea mover la pieza:")
                    movimiento_valido = self.validar_movimiento(pieza, origen, destino)

                pieza.mover(origen, destino, self.tablero.tablero)
                turno += 1

    def elegir_pieza(self, jugador, Posicion_pieza, mi_tablero):
        #obtenemos la pieza de la posicion dada
        valor_1 = Posicion_pieza[0]
        valor_2 = Posicion_pieza[1]
        if jugador.color != "blanco": 
            if mi_tablero [valor_1][valor_2] == "♟":
                return Peon(color=jugador.color)
            elif mi_tablero [valor_1][valor_2] == "♜":
                return Torre(color=jugador.color)
            elif mi_tablero [valor_1][valor_2] == "♞":
                return Caballo(color=jugador.color)
            elif mi_tablero [valor_1][valor_2] == "♝":
                return Alfil(color=jugador.color)
            elif mi_tablero [valor_1][valor_2] == "♛":
                return Reina(color=jugador.color)
            elif mi_tablero [valor_1][valor_2] == "♚":
                return Rey(color=jugador.color)
            elif mi_tablero [valor_1][valor_2] == " ":
                return
        else:    
            if mi_tablero [valor_1][valor_2] == "♙":
                return Peon(color=jugador.color)
            elif mi_tablero [valor_1][valor_2] == "♖":
                return Torre(color=jugador.color)
            elif mi_tablero [valor_1][valor_2] == "♘":
                return Caballo(color=jugador.color)
            elif mi_tablero [valor_1][valor_2] == "♗":
                return Alfil(color=jugador.color)
            elif mi_tablero [valor_1][valor_2] == "♕":
                return Reina(color=jugador.color)
            elif mi_tablero [valor_1][valor_2] == "♔":
                return Rey(color=jugador.color)
            elif mi_tablero [valor_1][valor_2] == " ":
                return
    


    def obtener_coordenadas(self, mensaje):
        fila = int(input(f"{mensaje} Fila: ")) - 1
        columna = int(input(f"{mensaje} Columna: ")) - 1
        return fila, columna

    def validar_movimiento(self, pieza, origen, destino):
        return pieza.mover(origen, destino, self.tablero.tablero)

juego = Juego()
juego.jugar()
