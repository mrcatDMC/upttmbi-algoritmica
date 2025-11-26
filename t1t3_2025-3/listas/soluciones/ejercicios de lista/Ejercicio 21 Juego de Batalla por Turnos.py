#Crea un sistema de batalla donde dos listas representan equipos de personajes que atacan por turnos. El personaje que sobrevive vuelve al final, el que muere es eliminado.
#Sistema de juego completo con lógica de batalla y gestión de listas.
# Cada personaje tiene 100 HP
# Daño aleatorio: 20-50 puntos
import random
import time
class Personaje:
    """Representa un personaje con nombre y puntos de vida (HP)."""
    def __init__(self, nombre):
        self.nombre = nombre
        self.hp = 100 

    def esta_vivo(self):
        """Verifica si el personaje tiene HP > 0."""
        return self.hp > 0

    def recibir_danio(self, danio):
        """Reduce el HP del personaje por el daño recibido."""
        self.hp = max(0, self.hp - danio)
        return danio

    def __str__(self):
        """Representación en string del personaje."""
        return f"**{self.nombre}** (HP: {self.hp})"

def generar_danio():
    """Genera un valor de daño aleatorio entre 20 y 50."""
    
    return random.randint(20, 50)

def turno_de_ataque(atacante, defensor):
    """
    Simula un turno de ataque.

    Devuelve:
    - True si el defensor fue eliminado.
    - False si el defensor sobrevivió.
    """
    danio = generar_danio()
    danio_recibido = defensor.recibir_danio(danio)

    print(f"🗡️ {atacante.nombre} ataca a {defensor.nombre}.")
    print(f"💥 {defensor.nombre} recibe **{danio_recibido}** puntos de daño.")
    
    if not defensor.esta_vivo():
        print(f"💀 **¡{defensor.nombre} ha sido ELIMINADO!**")
        return True
    else:
        print(f"🛡️  Estado: {defensor}")
        return False

def iniciar_batalla(equipo_a, equipo_b):
    """
    Ejecuta el ciclo principal de la batalla por turnos.
    """
    print("--- 🏁 ¡INICIO DE LA BATALLA! 🏁 ---")
    print(f"Equipo A (Héroes): {[p.nombre for p in equipo_a]}")
    print(f"Equipo B (Monstruos): {[p.nombre for p in equipo_b]}")
    print("-" * 35)
    
    turno = 1
    while equipo_a and equipo_b:
        print(f"\n===== TURNO {turno} =====")
        
        
        if equipo_a and equipo_b:
           
            atacante_a = equipo_a.pop(0) 
            
            defensor_b = equipo_b[0]      
            
            print(f"➡️ **Turno de {atacante_a.nombre} (Equipo A)**")
            defensor_b_eliminado = turno_de_ataque(atacante_a, defensor_b)
            
            if defensor_b_eliminado:
                equipo_b.pop(0) 
            
            
            equipo_a.append(atacante_a)
        
        
        if equipo_a and equipo_b: 
            
            atacante_b = equipo_b.pop(0)
            
            defensor_a = equipo_a[0]
            
            print(f"\n⬅️ **Turno de {atacante_b.nombre} (Equipo B)**")
            defensor_a_eliminado = turno_de_ataque(atacante_b, defensor_a)
            
            if defensor_a_eliminado:
                equipo_a.pop(0) 
                
            
            equipo_b.append(atacante_b)
        
        turno += 1
        time.sleep(0.5)

   
    print("\n--- 🏆 ¡FIN DE LA BATALLA! 🏆 ---")
    if equipo_a:
        print(f"🎉 **¡El Equipo A GANA!**")
        print(f"Sobrevivientes: {[str(p) for p in equipo_a]}")
    elif equipo_b:
        print(f"🎉 **¡El Equipo B GANA!**")
        print(f"Sobrevivientes: {[str(p) for p in equipo_b]}")
    else:
        print("🤝 ¡EMPATE! Ambos equipos fueron eliminados.")


if __name__ == "__main__":
    
    nombres_a = ["Guerrero", "Mago", "Arquero"]
    nombres_b = ["Orco", "Goblin", "Troll"]
    
   
    equipo_rojo = [Personaje(nombre) for nombre in nombres_a]
    equipo_azul = [Personaje(nombre) for nombre in nombres_b]
    
    
    iniciar_batalla(equipo_rojo, equipo_azul)