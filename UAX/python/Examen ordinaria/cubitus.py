import random

def tirada_jugador():
    tirada = []
    while True:
        dado = random.randint(1, 6)
        tirada.append(dado)
        if len(tirada) >= 2 and tirada[-1] == tirada[-2]:
            break
    return tirada

def main():
    print("JUEGO DE DADOS: HASTA REPETIR")

    tirada_cubitus = tirada_jugador()
    tirada_humerus = tirada_jugador()

    puntuacion_cubitus = tirada_cubitus[-1]
    puntuacion_humerus = tirada_humerus[-1]

    print(f"Tirada de Cubitus: {' '.join(map(str, tirada_cubitus))}")
    print(f"Tirada de Humerus: {' '.join(map(str, tirada_humerus))}")

    print(f"Cubitus ha sacado un {puntuacion_cubitus} y Humerus ha sacado un {puntuacion_humerus}.")

    if puntuacion_cubitus > puntuacion_humerus:
        print("Ha ganado Cubitus.")
    elif puntuacion_humerus > puntuacion_cubitus:
        print("Ha ganado Humerus.")
    else:
        print("Han empatado.")

if __name__ == "__main__":
    main()
