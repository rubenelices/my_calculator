###EJERCICIO DADOS###

import random

def valores():
    while True:
        valor1 = int(input("escoja un numero entre el 1 y el 6: "))
        if valor1 < 1 or valor1 > 6:
            print("Ese valor no esta en los dados")
        else:
            break

    while True:
        valor2 = int(input("escoja otro numero entre el 1 y el 6: "))
        if valor2 < 1 or valor2 > 6 or valor2 == valor1:
            print("Ese valor no esta permitido")
        else:
            break

    while True:
        valor3 = int(input("escoja un ultimo numero entre el 1 y el 6: "))
        if valor3 < 1 or valor3 > 6 or valor3 == valor2 or valor3 == valor1:
            print("Ese valor no esta permitido")
        else:
            break

    return valor1,valor2,valor3

def numero_de_dados():
    numdados = int(input("¿Cuantos dados quiere tirar?: "))
    if numdados < 1:
        print("¡Eso no tiene sentido!")
    return numdados

def tirar_dados(numdados):
    dados = [random.randint(1, 6) for _ in range(numdados)]
    print("Los dados han sido tirados y los  numeros que han salido son: ",dados )
    return dados

def puntuacion(dados, num1, num2, num3):
        puntos = dados.count(num1) + dados.count(num2) + dados.count(num3)
        return puntos

valor1, valor2, valor3 = valores()

# Obtener número de dados
numdados = numero_de_dados()

# Tirar los dados
dados = tirar_dados(numdados)

# Calcular puntuación
puntaje = puntuacion(dados, valor1,valor2,valor3)

print("Su puntuacion es: ",{puntaje})

def ganador():
    if puntaje > numdados/2 :
        print("¡Has ganado!")
    elif puntaje < numdados/2 :
        print("Has perdido...")
    elif puntaje == numdados/2 :
        print("Has empatado puto bot")
ganador()
