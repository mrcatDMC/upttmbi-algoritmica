#Simula una carrera donde los atletas pueden adelantarse. Modifica el orden según: Bruno adelanta 2 posiciones, Diana adelanta 1 posición.
atletas = ["Ana", "Bruno", "Carlos", "Diana", "Elena"]
while True:
    print("\nAtletas actuales en la carrera:", atletas)
    print("1- Bruno adelanta 2 posiciones")
    print("2- Diana adelanta 1 posición")
    print("3- Salir")
    opcion = input("Elige una opcion: ")
    if opcion == "1":
        indice_bruno = atletas.index("Bruno")
        if indice_bruno > 1:
            atletas.pop(indice_bruno)
            atletas.insert(indice_bruno - 2, "Bruno")
            print("Bruno ha adelantado 2 posiciones.")
        else:
            print("Bruno no puede adelantar más.")
    elif opcion == "2":
        indice_diana = atletas.index("Diana")
        if indice_diana > 0:
            atletas.pop(indice_diana)
            atletas.insert(indice_diana - 1, "Diana")
            print("Diana ha adelantado 1 posición.")
        else:
            print("Diana no puede adelantar más.")
    elif opcion == "3":
        print("Saliendo...")
        break
    else:
        print("Opcion no valida. Intenta de nuevo.")