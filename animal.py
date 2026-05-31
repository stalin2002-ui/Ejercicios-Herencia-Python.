class Animal:
    def __init__(self, especie, clase, longevidad):
        self.especie = especie
        self.clase = clase
        self.longevidad = longevidad

    def volar(self):
        print(f"La {self.especie} está volando")


class Aguila(Animal):
    def __init__(self, especie, clase, longevidad, envergadura, peso, velocidad):
        super().__init__(especie, clase, longevidad)
        self.envergadura = envergadura
        self.peso = peso
        self.velocidad = velocidad

    def mostrar_envergadura(self):
        print("Envergadura del águila:", self.envergadura)

    def mostrar_peso(self):
        print("Peso del águila:", self.peso)

    def mostrar_velocidad(self):
        print("Velocidad del águila:", self.velocidad)


aguila1 = Aguila("Águila Real", "Ave", "30 años", "2.3 metros", "6 kg", "320 km/h")

print("=== ÁGUILA ===")
aguila1.mostrar_envergadura()
aguila1.mostrar_peso()
aguila1.mostrar_velocidad()
