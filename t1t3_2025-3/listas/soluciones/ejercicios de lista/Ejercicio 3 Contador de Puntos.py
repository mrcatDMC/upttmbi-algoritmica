#ienes una lista de puntuaciones de un videojuego. Descubre cuántas veces obtuviste 100 puntos y en qué ronda fue la primera vez.
#Usar la lista de puntuaciones dada
#Contar cuántas veces aparece 100
#Encontrar en qué posición (ronda) fue la primera vez
#Mostrar resultados
puntuaciones = [50, 100, 75, 100, 90, 100, 60]
while True:
    print("\nPuntuaciones actuales:", puntuaciones)
    print("1- Contar veces que obtuviste 100 puntos")
    print("2- Encontrar la primera ronda con 100 puntos")
    print("3- Salir")
    opcion = input("Elige una opcion: ")
    if opcion == "1":
        veces_100 = puntuaciones.count(100)
        print(f"Has obtenido 100 puntos {veces_100} veces.")
    elif opcion == "2":
        if 100 in puntuaciones:
            primera_ronda = puntuaciones.index(100) + 1
            print(f"La primera vez que obtuviste 100 puntos fue en la ronda {primera_ronda}.")
        else:
            print("No has obtenido 100 puntos en ninguna ronda.")
    elif opcion == "3":
        print("Saliendo...")
        break
    else:
        print("Opcion no valida. Intenta de nuevo.")