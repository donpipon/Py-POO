
# multiplicar los numeros enteros positivos entre sí, a partir de una lista
def multiplicar(numeros: list) -> int:
    resultado = 1
    for numero in numeros:
        resultado *= numero
    return resultado

# funcion para ingresar una serie de numeros por consola y agregar a lista
def ingresar_numeros() -> list:
    numeros = []
    while True:
        numero = input()
        if numero.isnumeric():
            numeros.append(int(numero))
            continue
        else:
            break
    return numeros

operacion: str = input("Seleccione opcion:\n"
                  "1) Suma\n"
                  "2) Multiplicación\n"
                  "(cualquier otro input para salir)\n")

if operacion not in ("1","2"):
    exit()

elif operacion == "1":
    print("Elegiste opción 1) Suma")
    print("Ingrese numeros a sumar (cualquier letra o vacio para terminar):")

    numeros = ingresar_numeros()

    print(f'Resultado de la suma: {sum(numeros)}')

elif operacion == "2":
    print("Elegiste opción 2) Multiplicación")
    print("Ingrese numeros a multiplicar (cualquier letra o vacio para terminar):")

    numeros = ingresar_numeros()

    print(f'Resultado de la multiplicación: {multiplicar(numeros)}')
