class Vegetal:
    def __init__(self, nombre, reino, habitat):
        self.nombre = nombre
        self.reino = reino
        self.habitat = habitat

    def crecer(self):
        print(f"El vegetal {self.nombre} está creciendo")


class Arbol(Vegetal):
    def __init__(self, nombre, reino, habitat, altura, edad, tipo_hoja):
        super().__init__(nombre, reino, habitat)
        self.altura = altura
        self.edad = edad
        self.tipo_hoja = tipo_hoja

    def mostrar_altura(self):
        print("Altura del árbol:", self.altura)

    def mostrar_edad(self):
        print("Edad del árbol:", self.edad)

    def mostrar_tipo_hoja(self):
        print("Tipo de hoja:", self.tipo_hoja)


arbol1 = Arbol(
    "Roble",
    "Plantae",
    "Bosques templados",
    "30 metros",
    "100 años",
    "Hoja caduca"
)

print("=== ÁRBOL ===")
arbol1.mostrar_altura()
arbol1.mostrar_edad()
arbol1.mostrar_tipo_hoja()
