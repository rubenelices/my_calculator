### SUMA SIMPLE DE UNA MATRIZ ###

"""
Realizado por: Alejandro Barreche, Rubén Elices, Victor Valdivia
"""
# Se calcula el resultado que da la suma de los elementos de la matriz.
def simpleArraySum(matrix):
    return print(f"La suma de la matriz es: {sum(int(elem) for elem in matrix)}")

#Se establece el tamaño que tendrá la matriz, siendo siempre mayor que 0.
def get_matrix_size():
    while True:
        size = int(input("Introduzca cual va a ser el tamaño de la matriz: "))
        try:
            if size > 0:
                return size
            else:
                print("El tamaño de la matriz debe ser mayor que cero.")
        except ValueError:
            print("Por favor, ingresa un número válido para el tamaño.")

#Se introducen los números que van en la matriz y que serán sumados, tiene que haber tantos números como se haya indicado en el tamaño de la matriz sin exceder dicho número.

def matrix():
    size = get_matrix_size()
    while True:
        matrix_input = input("Introduzca los elementos de la matriz separados únicamente por espacios: ").rstrip().split()
        while len(matrix_input) != size:
            print("La dimensión de tu matriz no es correcta")
            matrix_input = input("Introduzca los elementos de la matriz separados únicamente por espacios: ").rstrip().split()
        try:
            matrix = [int(elem) for elem in matrix_input]
            return matrix
        except ValueError:
            print("Por favor, ingresa números enteros válidos.")

    
if __name__ == '__main__':
    simpleArraySum(matrix())
    