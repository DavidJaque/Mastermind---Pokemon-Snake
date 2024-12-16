from Pokemon import Pokemon


poke1 = Pokemon
poke2 = Pokemon

def fin_combate(poke1, poke2):
    print("Fin del combate")
    if poke1.getVida > poke2.getVida:
        print("Oh no!"+ poke2.getNombre() +  " se ha debilitado ( • ᴖ • ｡)")
        print(poke1.getNombre + " ha ganado! ૮ ˶ᵔ ᵕ ᵔ˶ ა")
    else:
        print("Oh no!" + poke1.getNombre + " se ha debilitado ( • ᴖ • ｡)")
        print(poke2.getNombre + " ha ganado! ૮ ˶ᵔ ᵕ ᵔ˶ ა")


print("\nComienza el combate!")


input("Presiona Enter para comenzar...\n")

while not poke1.debilitado() and not poke2.debilitado():
    #   COMBATEN

    #   Turno de Pokemon 1
    print("Turno de " + poke1.getNombre())

    poke1.mostrarAtaques()
    poke2.recibir_dano(poke2, poke1.atacar())

    if poke2.debilitado():
        fin_combate(poke1, poke2)
        exit()

    # mostrar barras de vida
    poke1.barras_de_vida()
    poke2.barras_de_vida()

    input("Enter para continuar...\n\n")


    #   Turno de Pokemon 2
    print("Turno de " + poke2.getNombre())

    poke2.mostrarAtaques()
    poke1.recibir_dano(poke1, poke2.atacar())

    if poke1.debilitado():
        fin_combate(poke1, poke2)
        exit()

    poke1.barras_de_vida()
    poke2.barras_de_vida()

    input("Enter para continuar...\n\n")



