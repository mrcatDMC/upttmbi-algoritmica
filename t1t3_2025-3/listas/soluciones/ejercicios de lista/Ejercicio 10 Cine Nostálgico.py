#Tienes películas con años de estreno. Ordénalas cronológicamente y luego "ve" (elimina) las 3 más antiguas una por una.
peliculas = [
    ("Matrix", 1999),
    ("Inception", 2010),
    ("Titanic", 1997),
    ("Avatar", 2009)
]
while True:
    print("\nPelículas actuales:")
    for titulo, anio in peliculas:
        print(f"{titulo} - {anio}")
    print("1- Ordenar películas cronológicamente")
    print("2- Ver (eliminar) las 3 películas más antiguas")
    print("3- Salir")
    opcion = input("Elige una opcion: ")
    if opcion == "1":
        peliculas_ordenadas = sorted(peliculas, key=lambda x: x[1])
        print("Películas ordenadas cronológicamente:")
        for titulo, anio in peliculas_ordenadas:
            print(f"{titulo} - {anio}")
    elif opcion == "2":
        peliculas_ordenadas = sorted(peliculas, key=lambda x: x[1])
        for _ in range(3):
            if peliculas_ordenadas:
                pelicula_vista = peliculas_ordenadas.pop(0)
                peliculas.remove(pelicula_vista)
                print(f"Has visto (eliminado): {pelicula_vista[0]} - {pelicula_vista[1]}")
            else:
                print("No hay más películas para ver.")
                break
    elif opcion == "3":
        print("Saliendo...")
        break
    else:
        print("Opcion no valida. Intenta de nuevo.")