#Tienes una lista con elementos duplicados y valores None. Crea una versión limpia sin duplicados ni valores nulos.
lista_sucia = [1, 2, None, 3, 2, 4, None, 1, 5, 3]
while True:
    print("\nLista actual:", lista_sucia)
    print("1- Limpiar la lista (eliminar duplicados y None)")
    print("2- Salir")
    opcion = input("Elige una opcion: ")
    if opcion == "1":
        lista_limpia = []
        for item in lista_sucia:
            if item is not None and item not in lista_limpia:
                lista_limpia.append(item)
        print("Lista limpia:", lista_limpia)
    elif opcion == "2":
        print("Saliendo...")
        break
    else:
        print("Opcion no valida. Intenta de nuevo.")