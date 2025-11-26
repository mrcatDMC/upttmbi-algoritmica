#Crea una función que genere 3 símbolos aleatorios. Determina si ganaste: 3 iguales = Jackpot, 2 iguales = Premio menor, todos diferentes = Sin premio.
import random
simbolos_posibles = ["🍒", "🍋", "🔔", "💎", "7️⃣"]
def jugar_tragamonedas():
    simbolos = [random.choice(simbolos_posibles) for _ in range(3)]
    return simbolos
while True:
    print("\nBienvenido a la Máquina Tragamonedas!")
    print("1- Jugar")
    print("2- Salir")
    opcion = input("Elige una opcion: ")
    if opcion == "1":
        resultado = jugar_tragamonedas()
        print("Resultado:", " | ".join(resultado))
        if resultado.count(resultado[0]) == 3:
            print("¡Jackpot! ¡Has ganado el premio mayor!")
        elif resultado.count(resultado[0]) == 2 or resultado.count(resultado[1]) == 2:
            print("¡Premio menor! ¡Has ganado un premio!")
        else:
            print("Sin premio. ¡Inténtalo de nuevo!")
    elif opcion == "2":
        print("Saliendo...")
        break
    else:
        print("Opcion no valida. Intenta de nuevo.")