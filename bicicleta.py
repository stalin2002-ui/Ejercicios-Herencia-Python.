class Transporte:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def arrancar(self):
        print(f"La {self.marca} {self.modelo} está lista para usarse")


class Bicicleta(Transporte):
    def __init__(self, marca, modelo, año, color, tipo, peso):
        super().__init__(marca, modelo, año)
        self.color = color
        self.tipo = tipo
        self.peso = peso

    def mostrar_color(self):
        print("Color de la bicicleta:", self.color)

    def mostrar_tipo(self):
        print("Tipo de bicicleta:", self.tipo)

    def mostrar_peso(self):
        print("Peso de la bicicleta:", self.peso)


bicicleta1 = Bicicleta("Trek", "Marlin 7", 2024, "Azul", "Montaña", "14 kg")

print("=== BICICLETA ===")
bicicleta1.mostrar_color()
bicicleta1.mostrar_tipo()
bicicleta1.mostrar_peso()
