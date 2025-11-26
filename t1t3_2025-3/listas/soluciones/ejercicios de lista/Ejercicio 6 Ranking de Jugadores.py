#Tienes una lista de puntajes desordenados. Crea un ranking de mayor a menor y muestra los 3 primeros lugares (medallistas de oro, plata y bronce).
#Usar la lista de puntajes dada
#Ordenar de mayor a menor
#Mostrar el top 3 (podio)
#Manejar empates correctamente
puntajes = [250, 300, 150, 400, 300, 200, 400]
while True:
    print("\nPuntajes actuales:", puntajes)
    print("1- Mostrar ranking de mayor a menor")
    print("2- Mostrar los 3 primeros lugares (podio)")
    print("3- Salir")
    opcion = input("Elige una opcion: ")
    if opcion == "1":
        puntajes_ordenados = sorted(puntajes, reverse=True)
        print("Ranking de mayor a menor:")
        for i, puntaje in enumerate(puntajes_ordenados, start=1):
            print(f"{i}. {puntaje}")
    elif opcion == "2":
        puntajes_ordenados = sorted(set(puntajes), reverse=True)
        podio = puntajes_ordenados[:3]
        print("Podio (Top 3):")
        for i, puntaje in enumerate(podio, start=1):
            medalla = "Oro" if i == 1 else "Plata" if i == 2 else "Bronce"
            print(f"{medalla}: {puntaje}")
    elif opcion == "3":
        print("Saliendo...")
        break
    else:
        print("Opcion no valida. Intenta de nuevo.")