###EJERCICIO 3###

# import random

# def tirar_dados():    
#     cubitus = [random.randint(1,6)],[random.randint(1,6)]
#     Humerus = [random.randint(1,6)],[random.randint(1,6)]
#     print("Las tiradas de cubitus han sido",cubitus)    
#     print("Las tiradas de Humerus han sido",Humerus)
   
# tirar_dados()

# def jugar(cubitus, Humerus): 
#     resultado_anterior = None
#     puntuacion = 0

#     while True:
#         valor_dado = tirar_dados()
#         print(f"{cubitus} tira un dado y obtiene un {valor_dado}")
#         print(f"{Humerus} tira un dado y obtiene un {valor_dado}")
#         if valor_dado == resultado_anterior:
#                 puntuacion = valor_dado
#                 break   
#         else:
#              resultado_anterior == valor_dado
#         return puntuacion
    
# cubitus , Humerus = jugar()

import random

def jugar_juego():
    print("Simulación de juego de dados")
    print("----------------------------")

    # Inicializar variables
    puntuacion_marcus = 0
    puntuacion_julius = 0

    # Definir la función para tirar un dado
    def tirar_dado():
        return random.randint(1, 6)

    # Función para jugar una ronda
    def jugar_ronda(jugador):
        resultado_anterior = None
        puntuacion = 0

        while True:
            valor_dado = tirar_dado()
            print(f"{jugador} tira un dado y obtiene un {valor_dado}")

            if valor_dado == resultado_anterior:
                puntuacion = valor_dado
                break
            else:
                resultado_anterior = valor_dado

        return puntuacion

    # Jugar ronda para Marcus
    puntuacion_marcus = jugar_ronda("Marcus")
    print(f"Puntuación de Marcus: {puntuacion_marcus}\n")

    # Jugar ronda para Julius
    puntuacion_julius = jugar_ronda("Julius")
    print(f"Puntuación de Julius: {puntuacion_julius}\n")

    # Determinar al ganador
    if puntuacion_marcus > puntuacion_julius:
        print("¡Marcus gana!")
    elif puntuacion_julius > puntuacion_marcus:
        print("¡Julius gana!")
    else:
        print("¡Es un empate!")

# Iniciar el juego
jugar_juego()
