#Crea una función que tome una lista de colores y: agregue "blanco" al inicio y "negro" al final, cree una versión invertida, y retorne ambas versiones.
#Practicar funciones con listas, insert() y reverse().
colores = ["rojo", "verde", "azul", "amarillo"]
lista = []
def modificar_lista(colores):
    lista = colores.copy()
    lista.insert(0, "blanco")
    lista.append("negro")
    lista_invertida = lista[::-1]
    return lista, lista_invertida
while True:
    print("\nLista de colores actual:", colores)
    print("1- Modificar lista de colores")
    print("2- Salir")
    opcion = input("Elige una opcion: ")
    if opcion == "1":
        lista_modificada, lista_invertida = modificar_lista(colores)
        print("Lista modificada:", lista_modificada)
        print("Lista invertida:", lista_invertida)
    elif opcion == "2":
        print("Saliendo...")
        break
    else:
        print("Opcion no valida. Intenta de nuevo.")