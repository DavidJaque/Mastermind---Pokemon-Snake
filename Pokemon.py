import random


class Pokemon:
    def __init__(self, nombre, vida, ataques, potencia_ataques):
        self.nombre = nombre
        self.vida = vida
        # Convertir ataques en una lista si no lo es ya
        self.ataques = ataques if isinstance(ataques, list) else ataques.split(",")
        self.vida_inicial = vida
        self.potencia_ataques = list(map(int, potencia_ataques.split(",")))

    def mostrarAtaques(self):   #   pendiente mostrar la potencia de los ataques
        if self.nombre == "Pikachu":
            print("¿Qué ataque deseas realizar?")

        for i in range(len(self.ataques)):
            print(f"[{i+1}] - {self.ataques[i]} [{self.potencia_ataques[i]}]")

    def atacar(self):
        self.mostrarAtaques()
        if self.nombre == "Pikachu":
            eleccion = int(input("Ingresa el número del ataque: "))
            if 1 <= eleccion <= len(self.ataques):
                print(f"\n{self.nombre} usa {self.ataques[eleccion - 1].strip()}!")
                return self.potencia_ataques[eleccion - 1]

            else:
                print("Error: ataque no válido")
        else:
            lista = [1,2,3,4]
            eleccion = random.choice(lista)
            print(f"\n{self.nombre} usa {self.ataques[eleccion - 1]}!")
            return self.potencia_ataques[eleccion - 1]

    def recibir_dano(self, dano):
        self.vida -= dano
        print(f"{self.nombre} recibió {dano} puntos de daño ")

    def barras_de_vida(self):
        # el 20 es por el largo de la barra de vida
        # genera una barra de vida basada en la vida actual
        barras = int(self.vida * 20 / self.vida_inicial)
        print(f"\n{self.nombre}")
        print(f"PS:   [{'*' * barras}{' ' * (20 - barras)}] ({self.vida}/{self.vida_inicial})")

    def debilitado(self):
        if self.vida <= 0:
            return True

    def getNombre(self):
        return self.nombre

    def getVida(self):
        return self.vida

