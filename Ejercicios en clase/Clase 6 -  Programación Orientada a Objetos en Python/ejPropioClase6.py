"""
Enunciado:

Cierta empresa requiere una app para administrar los datos de su personal,
del cual conoce DNI, nombre, apellido y año de ingreso. Existen dos categorias de empleados:
con salario fijo y a comisión. Los empleados a comision tienen un salario mínimo,
un número de clientes captados y un monto a cobrar por cada cliente captado.
El salario se optiene multiplicando los clientes captados y un monto a cobrar por cada uno.
Si el salario por comision no llega a cubrir el salario minimo, cobrará el salario mínimo.
Los empleados con salario fijo tienen un sueldo basico y un porcentaje adicional en funcion del numero de años
que llevan en la empresa:
- Menos de 2 años: nada
- de 2 a 5 años: 5% más
- más de 5 años: 10% mas.

Basado en el enunciado, realiza:

A) el diagrama de clases que lo modelice con sus relaciones, atributos y metodos
B) la implementacion del metodo mostrarSalarios que imprima por consolael nombre completo de cada empleado
junto a su salario-
C) La implementacion del metodo empleadoConMasClientes que devuelva al empleado con
mayor cantidad de clientes captados (se supone único).
"""


from datetime import datetime as dt
from enum import Enum

class TipoContrato(Enum):
    FIJO = "Fijo"
    COMISION = "Comision"

class Empleado:

    def __init__(self, dni: str, nombre: str, apellido: str, año_ingreso: int, tipo_contrato: TipoContrato):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.año_ingreso = año_ingreso
        self.tipo_contrato = tipo_contrato

    def mostrarSalario(self):
        pass

    def calcularSalarioTotal(self):
        pass

class EmpleadoComision(Empleado):
    def __init__(self, dni: str, nombre: str, apellido: str, año_ingreso: int, tipo_contrato: TipoContrato,
                 clientes_captados: int, monto_por_cliente: float, salario_minimo: float=170000):
        super().__init__(dni, nombre, apellido, año_ingreso, tipo_contrato)
        self.salario_minimo = salario_minimo
        self.clientes_captados = clientes_captados
        self.monto_por_cliente = monto_por_cliente

    #override method
    def mostrarSalario(self):
        print("-----------------------------------------------")
        print("Nombre completo: " + self.nombre + " " + self.apellido)
        print(f'Salario: ${self.calcularSalarioTotal()}')

    #override method
    def calcularSalarioTotal(self):
        if self.clientes_captados * self.monto_por_cliente >= self.salario_minimo:
            return self.clientes_captados * self.monto_por_cliente
        else:
            return self.salario_minimo

    @staticmethod
    def empleadoConMasClientes(empleados):
        empleado_con_mas_clientes = None
        max_clientes_captados = 0

        for empleado in empleados:
            if isinstance(empleado, EmpleadoComision):
                if empleado.clientes_captados > max_clientes_captados:
                    max_clientes_captados = empleado.clientes_captados
                    empleado_con_mas_clientes = empleado
        return  empleado_con_mas_clientes


class EmpleadoFijo(Empleado):
    def __init__(self, dni: str, nombre: str, apellido: str, año_ingreso: int, tipo_contrato: TipoContrato, salario: float):
        super().__init__(dni, nombre, apellido, año_ingreso, tipo_contrato)
        self.salario = salario

    #override method
    def mostrarSalario(self):
        print("-----------------------------------------------")
        print("Nombre completo: "+self.nombre+" "+self.apellido)
        print(f'Salario: ${self.calcularSalarioTotal()}')

    #override method
    def calcularSalarioTotal(self):
        if (dt.now().year - self.año_ingreso) >= 5:
            return  self.salario * 1.1
        elif (dt.now().year - self.año_ingreso) >= 2:
            return self.salario * 1.05
        else:
            return self.salario


if __name__ == "__main__":

    empleado1 = EmpleadoFijo(dni="20541826", nombre="Juan", apellido="Perez", año_ingreso=2021,
                             tipo_contrato=TipoContrato.FIJO, salario=180000)
    empleado2 = EmpleadoFijo(dni="42658798", nombre="Maria", apellido="Gonzalez", año_ingreso=2023,
                             tipo_contrato=TipoContrato.FIJO, salario=250000)
    empleado3 = EmpleadoFijo(dni="12365479", nombre="Pepe", apellido="Lopez", año_ingreso=2015,
                             tipo_contrato=TipoContrato.FIJO, salario=280000)
    empleado4 = EmpleadoFijo(dni="05897413", nombre="Gabriel", apellido="Wainraich", año_ingreso=2020,
                             tipo_contrato=TipoContrato.FIJO, salario=350000)
    empleado5 = EmpleadoFijo(dni="27958965", nombre="Josefina", apellido="Hopper", año_ingreso=2021,
                             tipo_contrato=TipoContrato.FIJO, salario=500000)
    empleado6 = EmpleadoComision(dni="31568497", nombre="Andres", apellido="Agnelli", año_ingreso=2022,
                             tipo_contrato=TipoContrato.COMISION, clientes_captados=0, monto_por_cliente=22500)
    empleado7 = EmpleadoComision(dni="31556889", nombre="Julian", apellido="Martinez", año_ingreso=2018,
                             tipo_contrato=TipoContrato.COMISION, clientes_captados=40, monto_por_cliente=5000)
    empleado8 = EmpleadoComision(dni="29584792", nombre="Bob", apellido="Johnson", año_ingreso=2024,
                             tipo_contrato=TipoContrato.COMISION, clientes_captados=12, monto_por_cliente=15000)
    empleado9 = EmpleadoComision(dni="25666558", nombre="Luisa", apellido="Lane", año_ingreso=2023,
                             tipo_contrato=TipoContrato.COMISION, clientes_captados=8, monto_por_cliente=35000)
    empleado10 = EmpleadoComision(dni="49581321", nombre="Washington", apellido="Sanchez", año_ingreso=2020,
                             tipo_contrato=TipoContrato.COMISION, clientes_captados=17, monto_por_cliente=55000)

    empleados = [empleado1, empleado2, empleado3, empleado4, empleado5, empleado6, empleado7, empleado8, empleado9, empleado10]

    for empleado in empleados:
        empleado.mostrarSalario()

    empleado_con_mas_clientes = EmpleadoComision.empleadoConMasClientes(empleados)
    print(f'\nEmpleado con mas clientes: {empleado_con_mas_clientes.nombre} {empleado_con_mas_clientes.apellido}'
          f' ({empleado_con_mas_clientes.clientes_captados} clientes captados)')

