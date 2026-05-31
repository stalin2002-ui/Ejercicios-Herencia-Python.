class MaterialEscolar:
    def __init__(self, nombre, marca, precio):
        self.nombre = nombre
        self.marca = marca
        self.precio = precio

    def usar(self):
        print(f"Usando {self.nombre} de marca {self.marca}")


class Cuaderno(MaterialEscolar):
    def __init__(self, nombre, marca, precio, color, hojas, tipo):
        super().__init__(nombre, marca, precio)
        self.color = color
        self.hojas = hojas
        self.tipo = tipo

    def mostrar_color(self):
        print("Color del cuaderno:", self.color)

    def mostrar_hojas(self):
        print("Número de hojas:", self.hojas)

    def mostrar_tipo(self):
        print("Tipo de cuaderno:", self.tipo)


cuaderno1 = Cuaderno("Cuaderno Universitario", "Norma", 3.50, "Rojo", 100, "Cuadriculado")

print("=== CUADERNO ===")
cuaderno1.mostrar_color()
cuaderno1.mostrar_hojas()
cuaderno1.mostrar_tipo()
