
class Bicicleta:

    def __init__(self, tipo: str, rodado: int, color: str):
        self.tipo = tipo
        self.rodado = rodado
        self.color = color

    def __str__(self):
        return f'Bicicleta de tipo {self.tipo}, rodado {self.rodado} de color {self.color}'

    def go(self):
        print("La bicicleta avanza")

    def stop(self):
        print("La bicicleta se detiene")



