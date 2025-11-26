#Organiza una lista de libros por número de páginas, del más corto al más largo.
libros = [
    {"titulo": "El Hobbit", "paginas": 310},
    {"titulo": "1984", "paginas": 328},
    {"titulo": "El Principito", "paginas": 96}
]
while True:
    print("\nLibros actuales:")
    for libro in libros:
        print(f"{libro['titulo']} - {libro['paginas']} páginas")
    print("1- Organizar libros por número de páginas (de más corto a más largo)")
    print("2- Salir")
    opcion = input("Elige una opcion: ")
    if opcion == "1":
        libros_ordenados = sorted(libros, key=lambda x: x['paginas'])
        print("Libros organizados por número de páginas:")
        for libro in libros_ordenados:
            print(f"{libro['titulo']} - {libro['paginas']} páginas")
    elif opcion == "2":
        print("Saliendo...")
        break
    else:
        print("Opcion no valida. Intenta de nuevo.")