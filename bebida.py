class Producto:
    def __init__(self, nombre, origen, categoria):
        self.nombre = nombre
        self.origen = origen
        self.categoria = categoria

    def describir(self):
        print(f"Producto: {self.nombre}")


class Bebida(Producto):
    def __init__(self, nombre, origen, categoria, volumen, sabor, temperatura):
        super().__init__(nombre, origen, categoria)
        self.volumen = volumen
        self.sabor = sabor
        self.temperatura = temperatura

    def mostrar_volumen(self):
        print("Volumen:", self.volumen)

    def mostrar_sabor(self):
        print("Sabor:", self.sabor)

    def mostrar_temperatura(self):
        print("Temperatura ideal:", self.temperatura)


bebida1 = Bebida("Jugo de Naranja", "Ecuador", "Natural", "500 ml", "Dulce", "Fría")

print("=== BEBIDA ===")
bebida1.mostrar_volumen()
bebida1.mostrar_sabor()
bebida1.mostrar_temperatura()
