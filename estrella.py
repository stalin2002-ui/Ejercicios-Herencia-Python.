class CuerpoCeleste:
    def __init__(self, nombre, tipo, distancia_tierra):
        self.nombre = nombre
        self.tipo = tipo
        self.distancia_tierra = distancia_tierra

    def describir(self):
        print(f"Cuerpo celeste: {self.nombre}")


class Estrella(CuerpoCeleste):
    def __init__(self, nombre, tipo, distancia_tierra, diametro, temperatura, edad):
        super().__init__(nombre, tipo, distancia_tierra)
        self.diametro = diametro
        self.temperatura = temperatura
        self.edad = edad

    def mostrar_diametro(self):
        print("Diámetro de la estrella:", self.diametro)

    def mostrar_temperatura(self):
        print("Temperatura:", self.temperatura)

    def mostrar_edad(self):
        print("Edad aproximada:", self.edad)


estrella1 = Estrella(
    "Sirio",
    "Estrella",
    "8.6 años luz",
    "2.4 millones km",
    "9,940 °C",
    "242 millones de años"
)

print("=== ESTRELLA ===")
estrella1.mostrar_diametro()
estrella1.mostrar_temperatura()
estrella1.mostrar_edad()
