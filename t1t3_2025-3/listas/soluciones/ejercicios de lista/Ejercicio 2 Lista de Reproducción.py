#Crea una playlist vacía. Agrega 5 canciones, luego pon tu canción favorita en la primera posición sin eliminar las demás.
#Crear una lista vacía llamada playlist
#Agregar 5 canciones usando append()
#Insertar una canción favorita al inicio usando insert()
#Mostrar la playlist completa
playlist = []
while True:
    print("\ncanciones actuales:", playlist)
    print("1- Agregar canciones")
    print("2- cancion favorita")
    print("3- Salir")
    opcion = input("Elige una opcion: ")
    if opcion == "1":
        for i in range(5):
            cancion = input("Ingresa el nombre de la cancion: ")
            playlist.append(cancion)
            print("Cancion agregada " + cancion)
    elif opcion == "2":
        cancion_fav = input("Ingresa el nombre de tu cancion favorita: ")
        if cancion_fav in playlist:
            playlist.remove(cancion_fav)
            playlist.insert(0, cancion_fav)
            print(f"Cancion '{cancion_fav}' puesta en la primera posicion.")
        else:
            print(f"Cancion '{cancion_fav}' no encontrada en la playlist.")
    elif opcion == "3":
        print("Saliendo...")
        break
    else:
        print("Opcion no valida. Intenta de nuevo.")