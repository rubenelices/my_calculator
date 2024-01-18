import random


num = int(input("Dime un número del 0 al 99: "))
while (num < 0) or (num > 99):
     print ("Ese número no es válido")
     num = int(input("Dime un número del 0 al 99: "))
  
ale = int(random.random()*100)

intentos = 0

while True:

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
    num = int(input("Dime un número del 0 al 99: "))
