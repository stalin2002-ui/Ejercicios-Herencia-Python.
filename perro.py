class Animal:
    def __init__(self, nombre, habitat, dieta):
        self.nombre = nombre
        self.habitat = habitat
        self.dieta = dieta

    def describir(self):
        print(f"Animal: {self.nombre}")


class Perro(Animal):
    def __init__(self, nombre, habitat, dieta, raza, peso, edad):
        super().__init__(nombre, habitat, dieta)
        self.raza = raza
        self.peso = peso
        self.edad = edad

    def mostrar_raza(self):
        print("Raza del perro:", self.raza)

    def mostrar_peso(self):
        print("Peso del perro:", self.peso)

    def mostrar_edad(self):
        print("Edad del perro:", self.edad)


perro1 = Perro("Max", "Casa", "Omnívoro", "Labrador", "30 kg", "5 años")

print("=== PERRO ===")
perro1.mostrar_raza()
perro1.mostrar_peso()
perro1.mostrar_edad()
