class Dispositivo:
    def __init__(self, marca, modelo, precio):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio

    def encender(self):
        print(f"Encendiendo {self.marca} {self.modelo}")


class Laptop(Dispositivo):
    def __init__(self, marca, modelo, precio, color, memoria_ram, procesador):
        super().__init__(marca, modelo, precio)
        self.color = color
        self.memoria_ram = memoria_ram
        self.procesador = procesador

    def mostrar_color(self):
        print("Color de la laptop:", self.color)

    def mostrar_memoria_ram(self):
        print("Memoria RAM:", self.memoria_ram)

    def mostrar_procesador(self):
        print("Procesador:", self.procesador)


laptop1 = Laptop("HP", "Pavilion 15", 750, "Plateado", "16 GB", "Intel Core i7")

print("=== LAPTOP ===")
laptop1.mostrar_color()
laptop1.mostrar_memoria_ram()
laptop1.mostrar_procesador()
