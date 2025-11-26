#Dos restaurantes se fusionan. Combina sus menús en uno solo y elimina los platos duplicados para que no aparezcan dos veces.
#Combinar ambos menús
#Eliminar duplicados
#Mostrar el menú fusionado
menu_restaurante_1 = ["Ensalada César", "Pizza Margherita", "Spaghetti Bolognese", "Tiramisú"]
menu_restaurante_2 = ["Sopa de Tomate", "Pizza Margherita", "Lasagna", "Gelato"]
while True:
    print("\nMenú Restaurante 1:", menu_restaurante_1)
    print("Menú Restaurante 2:", menu_restaurante_2)
    print("1- Fusionar menús")
    print("2- Salir")
    opcion = input("Elige una opcion: ")
    if opcion == "1":
        menu_fusionado = menu_restaurante_1 + menu_restaurante_2
        menu_sin_duplicados = list(set(menu_fusionado))
        print("Menú fusionado sin duplicados:")
        for plato in menu_sin_duplicados:
            print(plato)
    elif opcion == "2":
        print("Saliendo...")
        break
    else:
        print("Opcion no valida. Intenta de nuevo.")