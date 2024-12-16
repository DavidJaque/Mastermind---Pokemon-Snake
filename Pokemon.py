
class Pokemon:
    def __init__(self, nombre, vida, ataques, potencia_ataques):
        self.nombre = nombre
        self.vida = vida
        # Convertir ataques en una lista si no lo es ya
        self.ataques = ataques if isinstance(ataques, list) else ataques.split(",")
        self.vida_inicial = vida
        self.potencia_ataques = potencia_ataques if isinstance(potencia_ataques, list) else potencia_ataques.split(",")


    def mostrarAtaques(self):
        print("¿Qué ataque deseas realizar?")
        for i, ataque, potencia_ataque in enumerate(self.ataques, start=1):
            print(f"[{i}] - {ataque.strip()} ({potencia_ataque.strip()})")

    def atacar(self):
        self.mostrarAtaques()
        eleccion = int(input("Ingresa el número del ataque: "))
        if 1 <= eleccion <= len(self.ataques):
            print(f"{self.nombre} usa {self.ataques[eleccion - 1].strip()}!")
            return self.potencia_ataques[eleccion]

        else:
            print("Error: ataque no válido")

    def recibir_dano(self, dano_Recibido):
        self.vida -= dano_Recibido

    def barras_de_vida(self):
        # el 20 es por el largo de la barra de vida
        # genera una barra de vida basada en la vida actual
        barras = int(self.vida * 20 / self.vida_inicial)
        print(f"{self.nombre}")
        print(f"PS:   [{'*' * barras}{' ' * (20 - barras)}] ({self.vida}/{self.vida_inicial})")

    def debilitado(self):
        if self.vida <= 0:
            return True

    def getNombre(self):
        return self.nombre

    def getVida(self):
        return self.vida

