import random

def selecciona_un_nivel():
    print("1. Nivel simple (entre 0 y 100)")
    print("2. Nivel intermedio (entre 0 y 1000)")
    print("3. Nivel avanzado (entre 0 y 1000000)")
    print("4. Nivel experto (entre 0 y 1000000000)")

    while True:
        try:
            nivel_elegido = int(input("Ingresa el número del nivel: "))
            if 1 <= nivel_elegido <= 4:
                return nivel_elegido
            else:
                print("Por favor, ingresa un número válido (1, 2, 3, 4).")
        except ValueError:
            print("Por favor, ingresa un número válido.")



nivel_seleccionado = selecciona_un_nivel()

def num_intentos():
    while True:
        intentos = input("Dime cuantos intentos quieres tener: ")
        try:
            intentos = int(intentos)
            if intentos <= 0:
                print("Son muy pocos intentos")
                continue
            else:
                break
        except:
            print("Eso no es un número :)")
    return intentos


    
numero_de_intentos = num_intentos()
if (nivel_seleccionado == 1):
    num = int(input("Dime un número del 0 al 99: "))
    while (num < 0) or (num > 99):
     print ("Ese número no es válido")
     num = int(input("Dime un número del 0 al 99: "))
     ale = int(random.random()*100)
elif (nivel_seleccionado == 2):  
    num = int(input("Dime un número del 0 al 999: "))
    while (num < 0) or (num > 999):
     print ("Ese número no es válido")
     num = int(input("Dime un número del 0 al 999: "))
     ale = int(random.random()*1000)
elif (nivel_seleccionado == 3):  
    num = int(input("Dime un número del 0 al 999999: "))
    while (num < 0) or (num > 999999):
         print ("Ese número no es válido")
         num = int(input("Dime un número del 0 al 999999: "))
    ale = int(random.random()*1000000)
elif (nivel_seleccionado == 4):
    num = int(input("Dime un número del 0 al 999999999: "))
    while (num < 0) or (num > 999999999):
     print ("Ese número no es válido")
     num = int(input("Dime un número del 0 al 999999999: "))
     ale = int(random.random()*100000000)

intentos = 0

while intentos<numero_de_intentos -1:

    intentos += 1

    if ale < num:
        print("El número que estaba pensando es menor que el tuyo, ¡Prueba de nuevo!")

    if ale > num:
        print("El número que estaba pensando es mayor que el tuyo, ¡Prueba de nuevo!")
    elif num == ale:
        print("El numero en el que estaba pensando", num,"es el mismo que el tuyo, has ganado! :)")
        print("Has logrado ganar en :", intentos,"intentos")
        break

    print("Llevas :", intentos, "intentos")
    num = int(input("Vuelve a intentarlo: "))

if(intentos == numero_de_intentos -1):
    print("Has perdido, el numero era:",ale)

