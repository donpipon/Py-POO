
class Animal:

    def __init__(self, cantidad_patas: int, tipo: str):
        self.cantidad_patas = cantidad_patas
        self.tipo = tipo

    def comer(self):
        return "estoy comiendo"


class Perro(Animal):

    def __init__(self, nombre: str, raza: str, cantidad_patas: int, tipo: str):
        super().__init__(cantidad_patas, tipo)
        self.nombre = nombre
        self.raza = raza

    def correr(self):
        return "estoy corriendo"


class Aguila(Animal):

    def volar(self):
        return "estoy volando"


