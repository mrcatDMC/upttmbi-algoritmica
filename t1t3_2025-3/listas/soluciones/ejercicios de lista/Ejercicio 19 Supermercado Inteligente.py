#Crea un sistema de carrito de compras donde puedas agregar productos (pueden repetirse), calcular cantidades, eliminar uno a uno, y calcular total agrupando por producto.
carrito = []
precios = {"manzana": 2, "pan": 1.5, "leche": 3, "huevos": 4}
def mostrar_carrito():
    if not carrito:
        print("El carrito está vacío.")
    else:
        print("Carrito actual:")
        productos_contados = {}
        for item in carrito:
            if item in productos_contados:
                productos_contados[item] += 1
            else:
                productos_contados[item] = 1
        for producto, cantidad in productos_contados.items():
            print(f"- {producto}: {cantidad} unidad(es) a ${precios[producto]} cada una")
def calcular_total():
    total = 0
    productos_contados = {}
    for item in carrito:
        if item in productos_contados:
            productos_contados[item] += 1
        else:
            productos_contados[item] = 1
    for producto, cantidad in productos_contados.items():
        total += precios[producto] * cantidad
    return total
while True:
    print("\nOpciones del carrito de compras:")
    print("1- Agregar producto")
    print("2- Eliminar un producto")
    print("3- Mostrar carrito")
    print("4- Calcular total")
    print("5- Salir")
    opcion = input("Elige una opcion: ")
    if opcion == "1":
        producto = input("Ingresa el nombre del producto a agregar (manzana, pan, leche, huevos): ")
        if producto in precios:
            carrito.append(producto)
            print(f"{producto} ha sido añadido al carrito.")
        else:
            print("Producto no disponible.")
    elif opcion == "2":
        producto = input("Ingresa el nombre del producto a eliminar: ")
        if producto in carrito:
            carrito.remove(producto)
            print(f"Una unidad de {producto} ha sido eliminada del carrito.")
        else:
            print(f"No hay unidades de {producto} en el carrito.")
    elif opcion == "3":
        mostrar_carrito()
    elif opcion == "4":
        total = calcular_total()
        print(f"El total del carrito es: ${total}")
    elif opcion == "5":
        print("Saliendo del sistema de carrito de compras...")
        break
    else:
        print("Opcion no valida. Intenta de nuevo.")