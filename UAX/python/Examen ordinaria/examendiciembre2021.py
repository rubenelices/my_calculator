###EJERCICIO 1###

num1 = int(input("Diga un numero entre 0 y 999: "))

while True:
    if num1 > 999:
        print("Ese numero es mayor que lo que te he pedido,¡ME CAGO EN TU VIDA ESPABILA!")
        num1 = int(input("Diga un numero entre 0 y 999: "))

    elif num1 < 0:
        print("Ese numero es menor que lo que te he pedido,¡ME CAGO EN TI ESPABILA COÑO!")
        num1 = int(input("Diga un numero entre 0 y 999: "))

    else:
        break

num2 = int(input("Diga otro numero entre 0 y 999: "))

while True:
    if num2 > 999:
        print("Ese numero es mayor que lo que te he pedido,¡ME CAGO EN TU VIDA ESPABILA!")
        num2 = int(input("Diga otro numero entre 0 y 999: "))

    elif num2 < 0:
        print("Ese numero es menor que lo que te he pedido,¡ME CAGO EN TI ESPABILA COÑO!")
        num2 = int(input("Diga otro numero entre 0 y 999: "))

    else:
        break

cifras_num1 = ''.join(sorted(str(num1)))
cifras_num2 = ''.join(sorted(str(num2)))

def verficacion_cifras():
    if cifras_num1 == cifras_num2:
        print("Las cifas",cifras_num1,"son iguales aunque esten desordenadas")
    else:
        print("Las cifras no son iguales")

verficacion_cifras()