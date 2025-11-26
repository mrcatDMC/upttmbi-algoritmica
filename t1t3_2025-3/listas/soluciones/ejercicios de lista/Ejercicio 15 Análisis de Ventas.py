#Tienes ventas mensuales del año. Encuentra qué mes tuvo las ventas más altas, cuál fue su posición, y calcula el promedio anual.
ventas = [1200, 1500, 980, 2100, 1800, 1650, 2300, 1900, 1750, 2000, 2200, 2500]
meses = ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]
while True:
    print("\nVentas mensuales actuales:", ventas)
    print("1- Encontrar mes con ventas más altas")
    print("2- Calcular promedio anual de ventas")
    print("3- Salir")
    opcion = input("Elige una opcion: ")
    if opcion == "1":
        venta_maxima = max(ventas)
        indice_maximo = ventas.index(venta_maxima)
        mes_maximo = meses[indice_maximo]
        print(f"El mes con ventas más altas es {mes_maximo} con {venta_maxima} unidades vendidas.")
    elif opcion == "2":
        promedio_anual = sum(ventas) / len(ventas)
        print(f"El promedio anual de ventas es {promedio_anual:.2f} unidades.")
    elif opcion == "3":
        print("Saliendo...")
        break
    else:
        print("Opcion no valida. Intenta de nuevo.")