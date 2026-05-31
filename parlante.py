class EquipoAudio:
    def __init__(self, marca, modelo, precio):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio

    def activar(self):
        print(f"Parlante {self.marca} {self.modelo} activado")


class Parlante(EquipoAudio):
    def __init__(self, marca, modelo, precio, potencia, conexion, color):
        super().__init__(marca, modelo, precio)
        self.potencia = potencia
        self.conexion = conexion
        self.color = color

    def mostrar_potencia(self):
        print("Potencia:", self.potencia)

    def mostrar_conexion(self):
        print("Tipo de conexión:", self.conexion)

    def mostrar_color(self):
        print("Color del parlante:", self.color)


parlante1 = Parlante("JBL", "Charge 5", 180, "40 W", "Bluetooth", "Negro")

print("=== PARLANTE ===")
parlante1.mostrar_potencia()
parlante1.mostrar_conexion()
parlante1.mostrar_color()
