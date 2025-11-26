#Tienes una lista de eventos en orden cronológico. Muestra los eventos del más reciente al más antiguo. Luego crea una copia de esa lista para una línea temporal alternativa.
#Usar la lista de eventos dada
#Mostrar el orden original
#Invertir la lista
#Crear una copia de la lista invertida
#Demostrar que son listas independientes
eventos = ["Nacimiento", "Primer día de escuela", "Graduación", "Primer trabajo", "Matrimonio"]
while True:
    print("\nEventos actuales:", eventos)
    print("1- Mostrar eventos en orden original")
    print("2- Mostrar eventos del más reciente al más antiguo")
    print("3- Crear línea temporal alternativa")
    print("4- Salir")
    opcion = input("Elige una opcion: ")
    if opcion == "1":
        print("Eventos en orden original:")
        for evento in eventos:
            print(evento)
    elif opcion == "2":
        eventos_invertidos = eventos[::-1]
        print("Eventos del más reciente al más antiguo:")
        for evento in eventos_invertidos:
            print(evento)
    elif opcion == "3":
        linea_temporal_alternativa = eventos[::-1]
        print("Línea temporal alternativa creada.")
        print("Modificando la línea temporal alternativa...")
        linea_temporal_alternativa.append("Viaje al espacio")
        print("Línea temporal alternativa:", linea_temporal_alternativa)
        print("Lista original de eventos:", eventos)
    elif opcion == "4":
        print("Saliendo...")
        break
    else:
        print("Opcion no valida. Intenta de nuevo.")