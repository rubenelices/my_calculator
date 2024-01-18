#Ejercicio 1. Saludo
#nombre = str(input("Ingrese su nombre: "))
#print("¡Hola!", nombre , "Bienvendo a python")

#Ejercicio 2. Suma de dos numeros
#try:
 #   num = int(input("Escriba un número: "))
  #  num2 = int(input("Escriba el numero que desees que se sume al anterior: "))
   # suma = num + num2
    #print("La suma de tus números es:", suma ,)
#
#except ValueError:
 #   print("Eso no es un numero valido")

#Ejercicio 3. multiplicacion de un número

# try:
#     num = int(input("Ingrese un número: "))
#     print("La tabla de multilplicar de",num,"es: ")
#     for i in range(1,11):
#         resultado = num * i
#         print("el resultado es: ",num,"x",i,"=",resultado)
# except ValueError:
#     print("Ese numero no es valido")


#Ejercicio 5. Calculadora
# def calculadora():
#     try:
#         num = float(int(input("Dime el primer número que desees operar: ")))
#         num2 = float(int(input("Dime el número con el que deseas operarlo: ")))
#         suma = num + num2
#         resta = num - num2
#         multiplicacion = num * num2
#         division = num / num2 
#         calculo = str(input("Ahora escriba la operacion que deseas hacer(suma,resta,multiplicacion,division): "))

#         if calculo == "suma":
#             print("El resultado es: ",suma,)
#         elif calculo == "resta":
#             print("El resultado es: ",resta,)  
#         elif calculo == "multiplicacion":
#             print("El resultado es: ",multiplicacion,)
#         elif calculo == "division":
#             print("El resultado es: ",division,)  

#     except ValueError:
#         print("Ese numero no es valido")
# calculadora()


###BUCLES###
# Ejercicio 1: Números pares e impares
# print("Números pares:")
# for i in range(2, 11, 2):
#     print(i)

# print("\nNúmeros impares:")
# for i in range(1, 10, 2):
#     print(i)

#Ejercicio 2. suma de numeros
# while True:
#     num = int(input("Introduzca un número(sera sumado con el siguiente): "))
#     num2 = int(input("Introduzca el siguiente numero: "))
#     suma = num + num2
#     print("La suma de ambos es: ",suma,)
#     if num == 0 or num2 == 0:
#         print("Hasta aqui  el blucle pisha")
#         break

#Ejercicio 3.Tabla de multiplcar
# try:
#     num = int(input("Ingresa el numero del que deseas la tabla: "))
#     for i in range(1,21):
#         resultado = num * i
#         print("La tabla de multiplicar de ",num, "x",i, "es",resultado,)
# except ValueError:
#     print("Ese no es un numero valido")

#Ejercicio 4: contador regresivo
# def contador():
#     while True:
#         print("Comienza el contador:")
#         for i in range(11,0,-1):
#             print("Quedan",i,"segundos")
#             if i == 1:
#                 print("BOOM")
#         break
# contador()

#Ejercicio 5. Numeros pares
# def pares():
#     print("Aqui te proporciono una lista de los primeros10 numeros pares:")
#     for i in range(0,22,2):
#         print(i)

# pares()

#Ejercicio 6:Adivinar el numero(juego adivinar)
# import random
# def adivinar_numero():
#     num = int(input("Introduzca un numero del 0 al 100: "))
#     if num < 0 and num > 100:
#         print("Ese no es un numero valido, porfavor escoja otro")     
#         num = int(input("Introduzca un numero del 0 al 100")) 

#     ale = int(random.random()*100)

#     intentos = 0

#     while True:
#         intentos += 1
#         if num < ale:
#             print("El numero en el que estaba pensando es mayor que el tuyo")
#             num = int(input("Ingresa otro numero: "))
#         elif num > ale:
#             print("El numero en el que estaba pensando es menor que el tuyo")
#             num = int(input("Introduzca otro numero: "))
#         elif num == ale:
#             print("El numero en el que estaba pensando es el mismo que el tuyo,¡Felicidades, has ganado!")
#             print("Has hecho",intentos,"intentos")
#             break
            
# adivinar_numero()

###CLASES###
#Ejercicio 1 crear una clase basica. y EJercicio 2.Herencia
# class persona:
#     def __init__(self):
#         self.nombre = str(input("Introduzca su nombre y apellidos por favor: "))
#         print("Encantado de conocerte",self.nombre,)
    
#         self.edad = int(input("introduzca su edad por favor: "))
#         print("No te crees ni tu que tengas",self.edad,"pero bueno...")
#     def imprimir_datos(self):
#             print("Es decir, te llamas",self.nombre,"y tienes",self.edad,"años,¿verdad?")
# persona1 = persona()
# persona1.imprimir_datos()

# class Estudiante():
#      def __init__(self, universidad, carrera, genero):
#           self.universidad = universidad
#           self.carrera = carrera
#           self.genero = genero

# persona = Estudiante("UAX", "Ingenieria matematica", "masculino")
# print(type(persona))
# print(persona.universidad,persona.carrera,persona.genero)
        
# class examen:
#     def __init__(self, preguntas, punt, dificultad):
#         self.preguntas = preguntas
#         self.puntuacion = punt
#         self.dificultad = dificultad

#     def examen1(self):
#         print(self.preguntas,self.puntuacion,self.dificultad)

# class recuperacion(examen):
#     pass
# ex1 = recuperacion("Ocho preguntas","5 correctas","muy dificil")
# print(ex1.examen1())       

# class animal:
#     def __init__(self,nombre):
#         self.nombre = nombre

#     def hacer_sonido(self):
#         pass

# class perro(animal):
#     def hacer_sonido(self):
#         return "guau guau"
    
# class gato(animal):
#     def hacer_sonido(self):
#         return "miau miau"

# mi_perro = perro("sergi")
# mi_gato = gato("barreche")

# print(mi_perro.nombre, "hace el sonido", mi_perro.hacer_sonido())
# print(mi_gato.nombre,"hace el sonido",mi_gato.hacer_sonido())
    

###INTENTO AJEDREZ###
# class tablero:
#     def __init__(self):
#         self.tablero = [
#             ['♜', '♞', '♝', '♛', '♚', '♝', '♞', '♜'],
#             ['♟', '♟', '♟', '♟', '♟', '♟', '♟', '♟'],
#             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
#             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
#             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
#             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
#             ['♙', '♙', '♙', '♙', '♙', '♙', '♙', '♙'],
#             ['♖', '♘', '♗', '♕', '♔', '♗', '♘', '♖']
#         ]
    
#     def imprimir_tablero(self):
#         for fila in self.tablero:
#             print(" ".join(fila))
#         print()

###EJERCICIOS HERENCIAS###
#Ejercicio 1.Coche
# class coche:
#     def __init__(self, marca, color, modelo):
#         self.marca = marca
#         self.color = color
#         self.modelo = modelo
#         pass


# class automovil(coche):
#     def __init__(self, marca, color, modelo, puertas, asientos):
#         super().__init__(marca, color, modelo)
#         self.puertas = puertas
#         self.asientos = asientos

# mi_primer_coche = automovil("Mercedes","blanco","GLC","5 puertas","5 asientos")
# mi_segundo_coche = automovil("Land Rover","negro","DISCOVERY 3","6 puertas",("7 asientos"))

# print("Uno de mis coches es el", mi_primer_coche.marca, "de color", mi_primer_coche.color,
#       "es el modelo", mi_primer_coche.modelo, "con", mi_primer_coche.puertas, "y", mi_primer_coche.asientos)

# print("Uno de mis coches es el",mi_segundo_coche.marca)

#Ejercicio.ACABO DE DESPERTAR
# class tartaria:
#     def __init__(self, antartida, tesla, reptilianos):
#         self.antartida = antartida
#         self.toroide_electromagnetico = tesla
#         self.reptilianos = reptilianos
#         pass

# class mrTartaria(tartaria):
#     def __init__(self, antartida, tesla, reptilianos, elites):
#         super().__init__(antartida, tesla, reptilianos)
#         self.elites = elites


# la_antartida = mrTartaria("Nadie nunca ha podido sobrevolar la antartida, por que sera?","El toroide electromagnetico produce energia infinita que seria capaz de alimentar a toda la poblacion(lo eliminaron en el ultimo reset)","las grandes monarquias no estan formadas por reptilianos, si no que canalizan la energia de los reptilianos al mundo real,son el puente entre mundos","las grandes elites controlan todo lo que te puedes imaginar, no hay nada que no este controlado")

# print("Aqui estan unos de los grandes secretos que los de arriba no quieren que sepas: ",la_antartida.antartida,"\n",la_antartida.toroide_electromagnetico,"\n",la_antartida.reptilianos,"\n",la_antartida.elites)


#Ejercicio examen.Intento ajedrez

# class tablero:
#     def __init__(self):
#         self.tablero = [
#             ['♜', '♞', '♝', '♛', '♚', '♝', '♞', '♜'],
#             ['♟', '♟', '♟', '♟', '♟', '♟', '♟', '♟'],
#             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
#             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
#             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
#             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
#             ['♙', '♙', '♙', '♙', '♙', '♙', '♙', '♙'],
#             ['♖', '♘', '♗', '♕', '♔', '♗', '♘', '♖']
#         ]
        
#     def imprimir_tablero(self):
#         for fila in self.tablero:
#             print(" ".join(fila))
#         print()

import random

def valores():
    while True:
        valor1 = int(input("Escoja un número entre el 1 y el 6: "))
        if 1 <= valor1 <= 6:
            break
        else:
            print("Ese valor no está en el rango permitido.")

    while True:
        valor2 = int(input("Escoja otro número entre el 1 y el 6 (diferente al primero): "))
        if 1 <= valor2 <= 6 and valor2 != valor1:
            break
        else:
            print("Ese valor no está permitido.")

    while True:
        valor3 = int(input("Escoja un último número entre el 1 y el 6 (diferente a los anteriores): "))
        if 1 <= valor3 <= 6 and valor3 != valor2 and valor3 != valor1:
            break
        else:
            print("Ese valor no está permitido.")

    return valor1, valor2, valor3

def numero_de_dados():
    numdados = int(input("¿Cuántos dados quiere tirar?: "))
    if numdados < 1:
        print("¡Eso no tiene sentido!")
    return numdados

def tirar_dados(numdados):
    dados = [random.randint(1, 6) for _ in range(numdados)]
    print("Los dados han sido tirados y los números que han salido son:", dados)
    return dados

def puntuacion(dados, num1, num2, num3):
    puntos = dados.count(num1) + dados.count(num2) + dados.count(num3)
    return puntos

# Obtener valores del usuario
valor1, valor2, valor3 = valores()

# Obtener número de dados
numdados = numero_de_dados()

# Tirar los dados
dados = tirar_dados(numdados)

# Calcular puntuación
puntaje = puntuacion(dados, valor1, valor2, valor3)

# Mostrar el resultado
print(f"Su puntuación es: {puntaje}")

