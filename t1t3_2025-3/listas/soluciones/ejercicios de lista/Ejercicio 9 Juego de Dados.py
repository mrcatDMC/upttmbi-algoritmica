#Simula 20 lanzamientos de dados (números del 1-6). Muestra cuántas veces salió cada número.
import random
lanzamientos = [random.randint(1, 6) for _ in range(20)]
while True:
    print("\nLanzamientos actuales:", lanzamientos)
    print("1- Mostrar cuántas veces salió cada número (1-6)")
    print("2- Salir")
    opcion = input("Elige una opcion: ")
    if opcion == "1":
        for numero in range(1, 7):
            veces = lanzamientos.count(numero)
            print(f"El número {numero} salió {veces} veces.")
    elif opcion == "2":
        print("Saliendo...")
        break
    else:
        print("Opcion no valida. Intenta de nuevo.")