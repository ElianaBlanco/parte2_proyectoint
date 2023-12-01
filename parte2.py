# Pedir el nombre del jugador por teclado
nombre_jugador = input("Ingresa tu nombre: ")

# Imprimir un mensaje de bienvenida con el nombre del jugador
print("¡Bienvenido,", nombre_jugador + "! Disfruta del juego.")

import readchar

def main():
    print("Presiona la tecla ↑ para salir.")
    
    while True:
        # Lee un carácter del teclado
        key = readchar.readkey()

        # Imprime el carácter
        print(f"Tecla presionada: {key}")

        # Comprueba si la tecla es la flecha l funciona
        if key.lower() == 'l':
            print("¡Tecla 'l' presionada! Saliendo del bucle.")
            break

if __name__ == "__main__":
    main()
