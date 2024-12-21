class Combate:
    def __init__(self, pokemon1, pokemon2):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2

    def iniciar(self, atacante, defensor):
        print("\nComienza el combate!")
        input("Presiona Enter para comenzar...\n")

        while not atacante.debilitado() and not defensor.debilitado():
            # Turno del atacante
            if self.turno(atacante, defensor):
                return
            # Turno del defensor
            if self.turno(defensor, atacante):
                return

    def mostrar_vida(self, atacante, defensor):
        atacante.barras_de_vida()
        defensor.barras_de_vida()

    def turno(self, atacante, defensor):
        print(f"Turno de {atacante.getNombre()}\n")
        dano = atacante.atacar()
        defensor.recibir_dano(dano)

        if defensor.debilitado():
            print("\nOh no! " + defensor.getNombre() + " se ha debilitado ( • ᴖ • ｡)")
            self.fin_combate(atacante, defensor)
            return True

        self.mostrar_vida(atacante, defensor)
        input("\nEnter para continuar...\n")
        return False

    def fin_combate(self, atacante, defensor):
        print("Fin del combate")
        if atacante.getVida() > defensor.getVida():
            print(f"\n{atacante.getNombre()} ha ganado! ૮ ˶ᵔ ᵕ ᵔ˶ ა")
        else:
            print(f"\n{defensor.getNombre()} ha ganado! ૮ ˶ᵔ ᵕ ᵔ˶ ა")
