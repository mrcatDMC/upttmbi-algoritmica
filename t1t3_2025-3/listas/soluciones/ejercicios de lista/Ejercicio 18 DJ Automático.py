#Crea una función que gestione una cola de reproducción musical: agregar álbumes, reproducir siguiente, agregar urgentes, mostrar próximas 3.
cola_reproduccion = []
def mostrar_proximos(cola):
    print("Próximos 3 álbumes en la cola:")
    for album in cola[:3]:
        print("-", album)
while True:
    print("\nCola de reproducción actual:", cola_reproduccion)
    print("1- Agregar álbum al final de la cola")
    print("2- Reproducir siguiente álbum")
    print("3- Agregar álbum urgente al inicio de la cola")
    print("4- Mostrar próximos 3 álbumes")
    print("5- Salir")
    opcion = input("Elige una opcion: ")
    if opcion == "1":
        album = input("Ingresa el nombre del álbum a agregar: ")
        cola_reproduccion.append(album)
        print(f"Álbum '{album}' agregado al final de la cola.")
    elif opcion == "2":
        if cola_reproduccion:
            album_siguiente = cola_reproduccion.pop(0)
            print(f"Reproduciendo álbum: '{album_siguiente}'")
        else:
            print("La cola está vacía. No hay álbumes para reproducir.")
    elif opcion == "3":
        album_urgente = input("Ingresa el nombre del álbum urgente a agregar: ")
        cola_reproduccion.insert(0, album_urgente)
        print(f"Álbum urgente '{album_urgente}' agregado al inicio de la cola.")
    elif opcion == "4":
        mostrar_proximos(cola_reproduccion)
    elif opcion == "5":
        print("Saliendo...")
        break
    else:
        print("Opcion no valida. Intenta de nuevo.")