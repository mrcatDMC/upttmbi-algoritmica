#Tienes una lista de números del 1 al 10. "Haz desaparecer" el último número y guárdalo, luego haz lo mismo con el primero. Muestra cuántos números quedan y cuáles desaparecieron.
#Crear lista de números del 1 al 10
#Usar pop() para eliminar y guardar el último número
#Usar pop(0) para eliminar y guardar el primero
#Mostrar los números que "desaparecieron"
#Mostrar los números restantes
numeros = list(range(1, 11))
while True:
    print("\nNúmeros actuales:", numeros)
    print("1- Hacer desaparecer el último número")
    print("2- Hacer desaparecer el primer número")
    print("3- Salir")
    opcion = input("Elige una opcion: ")
    if opcion == "1":
        if numeros:
            ultimo_numero = numeros.pop()
            print(f"Número '{ultimo_numero}' ha desaparecido.")
        else:
            print("No hay números para desaparecer.")
    elif opcion == "2":
        if numeros:
            primer_numero = numeros.pop(0)
            print(f"Número '{primer_numero}' ha desaparecido.")
        else:
            print("No hay números para desaparecer.")
    elif opcion == "3":
        print("Saliendo...")
        break
    else:
        print("Opcion no valida. Intenta de nuevo.")
    print(f"Números restantes ({len(numeros)}): {numeros}")