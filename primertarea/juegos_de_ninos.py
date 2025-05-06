import random

def obtener_opcion_usuario():
    opciones = ["piedra", "papel", "tijeras"]
    while True:
        usuario = input("Elige piedra, papel o tijeras (o escribe 'salir' para terminar): ").lower()
        if usuario in opciones or usuario == "salir":
            return usuario
        else:
            print("Opción no válida. Intenta de nuevo.")

def obtener_opcion_computadora():
    return random.choice(["piedra", "papel", "tijeras"])

def determinar_ganador(usuario, computadora):
    if usuario == computadora:
        return "Empate"
    elif (
        (usuario == "piedra" and computadora == "tijeras") or
        (usuario == "papel" and computadora == "piedra") or
        (usuario == "tijeras" and computadora == "papel")
    ):
        return "¡Ganaste!"
    else:
        return "Perdiste."

def jugar():
    print("Bienvenido al juego de Piedra, Papel o Tijeras.")
    while True:
        usuario = obtener_opcion_usuario()
        if usuario == "salir":
            print("¡Gracias por jugar!")
            break
        computadora = obtener_opcion_computadora()
        print(f"La computadora eligió: {computadora}")
        resultado = determinar_ganador(usuario, computadora)
        print(resultado)
        print("-" * 30)

# Ejecutar el juego
jugar()
