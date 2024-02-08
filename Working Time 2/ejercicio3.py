class Vehiculo:

    def __init__(self, tipo: str, color: str, marca: str):
        self.tipo = tipo
        self.color = color
        self.marca = marca


class Persona:

    def __init__(self, nombre: str, apellido: str, edad: int, profesion: str, vehiculo: Vehiculo):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.profesion = profesion
        self.vehiculo = vehiculo


persona1 = Persona(
    nombre="Juan",
    apellido="Lopez",
    edad=25,
    profesion="Abogado",
    vehiculo=Vehiculo(
        tipo="bicicleta",
        color="amarilla",
        marca="Massino"
    )
)

print(f'"{persona1.nombre} {persona1.apellido} tiene {persona1.edad} años y es de profesión {persona1.profesion}. Por la\n'
      f'tarde, después de trabajar, sale a camninar. También tiene una\n'
      f'{persona1.vehiculo.tipo} {persona1.vehiculo.color} marca {persona1.vehiculo.marca} y a veces sale a dar\n'
      f'vueltas en ella".')





