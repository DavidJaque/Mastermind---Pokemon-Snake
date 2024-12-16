
def __init__(self, pokemon1, pokemon2):
    self.pokemon1 = pokemon1
    self.pokemon2 = pokemon2


def iniciar(self):
    print("\nComienza el combate!")

    input("Presiona Enter para comenzar...\n")

    while not self.pokemon1.debilitado() and not self.pokemon2.debilitado():
        #   COMBATEN
        if self.turno(self.pokemon1, self.pokemon2):
            return
        if self.turno(self.pokemon2, self.pokemon1):
            return


def mostrar_vida(self):
    self.pokemon1.barras_de_vida()
    self.pokemon2.barras_de_vida()


def turno(self, atacante, defensor):
    print("Turno de " + atacante.getNombre())
    atacante.mostrarAtaques()
    dano = atacante.atacar()
    defensor.recibir_dano(dano)

    if defensor.debilitado():
        self.fin_combate()
        return True

    self.mostrar_vida()
    input("Enter para continuar...\n\n")
    return False


def fin_combate(self):
    print("Fin del combate")
    if self.pokemon1.getVida() > self.pokemon2.getVida():
        print("Oh no!"+ self.pokemon2.getNombre() +  " se ha debilitado ( • ᴖ • ｡)")
        print(self.pokemon1.getNombre() + " ha ganado! ૮ ˶ᵔ ᵕ ᵔ˶ ა")
    else:
        print("Oh no!" + self.pokemon1.getNombre() + " se ha debilitado ( • ᴖ • ｡)")
        print(self.pokemon2.getNombre() + " ha ganado! ૮ ˶ᵔ ᵕ ᵔ˶ ა")







