import random

def escape_probability(n, m, k, laberinto, tuneles):
    def is_valid(x, y):
        return 0 <= x < n and 0 <= y < m

    def is_free(x, y):
        return is_valid(x, y) and laberinto[x][y] == '.'

    def can_escape(x, y):
        return is_free(x, y) or laberinto[x][y] == '%'

    def traverse(x, y):
        if not is_valid(x, y) or laberinto[x][y] == 'X':
            return 0

        if laberinto[x][y] == '%':
            return 1

        laberinto[x][y] = 'X'

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        total_paths = 0

        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if can_escape(new_x, new_y):
                total_paths += traverse(new_x, new_y)

        return total_paths

    start_x, start_y = -1, -1
    for i in range(n):
        for j in range(m):
            if laberinto[i][j] == 'A':
                start_x, start_y = i, j

    if start_x == -1 or start_y == -1:
        print("Error: No se encontró la posición inicial 'A' en el laberinto.")
        return 0

    escape_paths = 0

    for _ in range(10000):  # Realiza simulaciones para estimar la probabilidad
        escape_paths += traverse(start_x, start_y)

    return escape_paths / 10000

# Mensajes explicativos
print("Ingresa las dimensiones del laberinto (n m k):")
n, m, k = map(int, input().split())

# Representación del laberinto
print("Ingresa la representación del laberinto (usando caracteres):")
laberinto = [list(input().strip()) for _ in range(n)]

# Imprimir coordenadas
print("\nLas celdas estarán representadas por sus coordenadas:")
for i in range(n):
    for j in range(m):
        print(f"({i},{j})", end="")
    print()

# Leer coordenadas de los túneles
tuneles = []
for _ in range(k):
    print("Ingresa las coordenadas de la entrada del túnel (i j):")
    entrada_tunel = tuple(map(int, input().split()))
    tuneles.append(entrada_tunel)

# Calcular e imprimir la probabilidad de escape
probability = escape_probability(n, m, k, laberinto, tuneles)
print(f"\nProbabilidad de escape: {probability:7f}")



