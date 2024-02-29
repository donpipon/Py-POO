"""
Una fábrica de instrumentos musicales posee una lista con todas sus sucursales.
Cada sucursal tiene su nombre y una lista con todos los instrumentos a la venta.
De cada uno de ellos se sabe su ID alfanumérico, su precio y su tipo
(Percusión, Viento o Cuerda).

Puntos a desarrollar

1)Desarrollar el diagrama de clases UML que modele lo enunciado y donde consten
las clases con sus atributos, métodos y relaciones (los constructores pueden omitirse).

2) Crear un proyecto en Python que resuelva:
    A) La explotación del método listarInstrumentos que muestre en la consola todos los
    datos de cada uno de los instrumentos.
    B) La explotación del método instrumentosPorTipo que devuelva una lista de
    instrumentos cuyo tipo coincida con el recibido por parámetro.
    C) La explotación del método borrarInstrumento que reciba un ID y elimine el
    instrumento asociado a tal ID de la sucursal donde se encuentre.
    D) La explotación del método porcInstrumentosPorTipo que reciba el nombre de una
    sucursal y retorne los porcentajes de instrumentos por tipo que hay para tal sucursal.

"""
import random
from enum import Enum

class TipoInstrumento(Enum):
    PERCUSION = "Percusion"
    VIENTO = "Viento"
    CUERDA = "Cuerda"

class Fabrica:

    def __init__(self):
        self.sucursales = []

    def agregarSucursal(self, sucursal) -> None:
        self.sucursales.append(sucursal)

    def listarInstrumentos(self) -> None:
        print("\nLista de Instrumentos:")
        for sucursal in self.sucursales:
            print(f'Sucursal {sucursal.nombre}:')
            for instrumento in sucursal.instrumentos:
                print(f'Id: {instrumento.id}, Precio: ${instrumento.precio}, Tipo: {instrumento.tipoInstrumento.value}')

    def instrumentosPorTipo(self, tipoInstrumento) -> list:
        lista_de_instrumentos_por_tipo = []
        for sucursal in self.sucursales:
            for instrumento in sucursal.instrumentos:
                if instrumento.tipoInstrumento == tipoInstrumento:
                    lista_de_instrumentos_por_tipo.append((instrumento, sucursal.nombre))
        return lista_de_instrumentos_por_tipo

    def porcInstrumentosPorTipo(self, nombre) -> dict:
        tipos = []
        for sucursal in self.sucursales:
            if sucursal.nombre == nombre:
                for instrumento in sucursal.instrumentos:
                    tipos.append(instrumento.tipoInstrumento)

        porc_percu = round((tipos.count(TipoInstrumento.PERCUSION) / len(tipos)) * 100)
        porc_viento = round((tipos.count(TipoInstrumento.VIENTO) / len(tipos)) * 100)
        porc_cuerda = round((tipos.count(TipoInstrumento.CUERDA) / len(tipos)) * 100)

        return {'Percusión': porc_percu, 'Viento': porc_viento, 'Cuerda': porc_cuerda}


class Sucursal:

    def __init__(self, id: str, nombre: str):
        self.__id = id
        self.nombre = nombre
        self.instrumentos = []

    def agregarInstrumento(self, instrumento) -> None:
        self.instrumentos.append(instrumento)

    def borrarInstrumento(self, id: str) -> None:
        instrumento_encontrado = False
        for instrumento in self.instrumentos:
            if instrumento.id == id:
                print(f'* Instrumento {id} eliminado *')
                self.instrumentos.remove(instrumento)
                instrumento_encontrado = True
                break
        if not instrumento_encontrado:
            print(f'[ERROR] - El instrumento con Id"{id}" no se encuentra en sucursal {self.nombre}')


class Instrumento:

    def __init__(self, id: str, precio: float, tipoInstrumento: TipoInstrumento):
        self.id = id
        self.precio = precio
        self.tipoInstrumento = tipoInstrumento


if __name__ == "__main__":

    #instancia de fabrica
    fabrica1 = Fabrica()

    #instancias de sucursales
    sucursal1 = Sucursal("01", "Boedo")
    sucursal2 = Sucursal("02", "Palermo")
    sucursal3 = Sucursal("03", "Calamuchita")

    #instancias de instrumentos
    instrumento1 = Instrumento("001", 5000, TipoInstrumento.PERCUSION)
    instrumento2 = Instrumento("002", 15000, TipoInstrumento.PERCUSION)
    instrumento3 = Instrumento("003", 50000, TipoInstrumento.CUERDA)
    instrumento4 = Instrumento("004", 560000, TipoInstrumento.VIENTO)
    instrumento5 = Instrumento("005", 100000, TipoInstrumento.PERCUSION)
    instrumento6 = Instrumento("006", 800000, TipoInstrumento.PERCUSION)
    instrumento7 = Instrumento("007", 25000, TipoInstrumento.CUERDA)
    instrumento8 = Instrumento("008", 95000, TipoInstrumento.CUERDA)
    instrumento9 = Instrumento("009", 1505000, TipoInstrumento.VIENTO)

    #asignar instrumentos a sucursales
    sucursal1.agregarInstrumento(instrumento1)
    sucursal1.agregarInstrumento(instrumento2)
    sucursal1.agregarInstrumento(instrumento3)
    sucursal2.agregarInstrumento(instrumento4)
    sucursal2.agregarInstrumento(instrumento5)
    sucursal2.agregarInstrumento(instrumento6)
    sucursal3.agregarInstrumento(instrumento7)
    sucursal3.agregarInstrumento(instrumento8)
    sucursal3.agregarInstrumento(instrumento9)

    #asignar sucursales a fabrica madre
    fabrica1.agregarSucursal(sucursal1)
    fabrica1.agregarSucursal(sucursal2)
    fabrica1.agregarSucursal(sucursal3)

    #Generar listado de instrumentos
    fabrica1.listarInstrumentos()

    #Generar y mostrar lista de instrumentos por tipo
    lista_instrumentos_percusion = fabrica1.instrumentosPorTipo(TipoInstrumento.PERCUSION)
    print(f'------------------------------------\n'
          f'Listado de instrumentos de Percusión')
    for instrumento, nombre_sucursal in lista_instrumentos_percusion:
        print(f'- ID: {instrumento.id}, Precio: ${instrumento.precio} (Sucursal {nombre_sucursal})')
    print(f'------------------------------------')

    #BORRAR INSTRUMENTO "001"
    sucursal1.borrarInstrumento("001")

    # Generar y mostrar lista actualizada, despues de borrar el instrumento 001
    lista_instrumentos_percusion = fabrica1.instrumentosPorTipo(TipoInstrumento.PERCUSION)
    print(f'------------------------------------\n'
          f'Listado de instrumentos de Percusión')
    for instrumento, nombre_sucursal in lista_instrumentos_percusion:
        print(f'- ID: {instrumento.id}, Precio: ${instrumento.precio} (Sucursal {nombre_sucursal})')
    print(f'------------------------------------')

    #calcular porcentajes de instrumento por tipo, por cada sucursal y mostrar a consola
    for sucursal in fabrica1.sucursales:
        porcentajes = fabrica1.porcInstrumentosPorTipo(sucursal.nombre)
        print(f'Porcentaje de instrumentos por tipo en sucursal {sucursal.nombre}:\n'
              f'Percusión: {porcentajes["Percusión"]}%\n'
              f'Viento: {porcentajes["Viento"]}%\n'
              f'Cuerda: {porcentajes["Cuerda"]}%\n')




















