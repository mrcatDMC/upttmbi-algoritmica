#Tienes una lista de ingredientes para pizza. Agrega 3 ingredientes más, elimina las anchoas (nadie las quiere), y muestra el resultado final.
#El programa debe:
#Partir de la lista dada
#Agregar 3 ingredientes nuevos
#Eliminar "anchoas"
#Mostrar la lista final
import time
ingredientes = ["queso", "tomate", "anchoas", "jamon"]
ingrediente_a_eliminar = "anchoas"
ingredientes_a_agregar = ["pepperoni", "pimientos", "aceitunas"]
while True:
    print("\nIngredientes actuales:", ingredientes)
    print("1- Agregar ingredientes")
    print("2- Eliminar ingrediente no deseado")
    print("3- Salir")
    opcion = input("Elige una opcion: ")
    if opcion == "1":
        for ingrediente in ingredientes_a_agregar:
            time.sleep(1)
            print("Ingrediente a agregar:" ,ingrediente,)
            c = input("quieres agregar si o no:")
            if c == "si":
                ingredientes.append(ingrediente)
                print("Ingredientes agregados")
            else:
                print("No se agrego ningun ingrediente")
    elif opcion == "2":
        time.sleep(1)
        if ingrediente_a_eliminar in ingredientes:
            ingredientes.remove(ingrediente_a_eliminar)
            print(f"Ingrediente '{ingrediente_a_eliminar}' eliminado.")
        else:
            print(f"Ingrediente '{ingrediente_a_eliminar}' no encontrado.")
    elif opcion == "3":
        time.sleep(1)
        print("Saliendo...")
        break
    else:
        print("Opcion no valida. Intenta de nuevo.")