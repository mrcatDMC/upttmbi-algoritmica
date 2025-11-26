#Crea un sistema de inventario para un juego RPG que permita: recoger objetos, verificar cantidad, usar/vender objetos, y organizar alfabéticamente.
inventario = []
def mostrar_inventario():
    if not inventario:
        print("El inventario está vacío.")
    else:
        print("Inventario actual:")
        for item in sorted(inventario):
            print(f"- {item} (Cantidad: {inventario.count(item)})")
while True:
    print("\nOpciones de inventario:")
    print("1- Recoger objeto")
    print("2- Ver cantidad de un objeto")
    print("3- Usar/Vender objeto")
    print("4- Mostrar inventario organizado alfabéticamente")
    print("5- Salir")
    opcion = input("Elige una opcion: ")
    if opcion == "1":
        objeto = input("Ingresa el nombre del objeto a recoger: ")
        inventario.append(objeto)
        print(f"{objeto} ha sido añadido al inventario.")
    elif opcion == "2":
        objeto = input("Ingresa el nombre del objeto para verificar cantidad: ")
        cantidad = inventario.count(objeto)
        print(f"Tienes {cantidad} unidad(es) de {objeto}.")
    elif opcion == "3":
        objeto = input("Ingresa el nombre del objeto a usar/vender: ")
        if objeto in inventario:
            inventario.remove(objeto)
            print(f"{objeto} ha sido usado/vendido.")
        else:
            print(f"No tienes {objeto} en el inventario.")
    elif opcion == "4":
        mostrar_inventario()
    elif opcion == "5":
        print("Saliendo del sistema de inventario...")
        break
    else:
        print("Opcion no valida. Intenta de nuevo.")