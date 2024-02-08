
# lista con 5 elementos de distinto tipo.
mi_lista = [1, "hola", True, {'nombre': "Andres"}, 42]

# imprimir el último elemento
print(mi_lista[-1])

# modificar el valor del tercer elemento
mi_lista[2] = False
print(mi_lista)

# agregar dos elementos             # opción alternativa:
mi_lista.extend(["B", "Python"])    # mi_lista = mi_lista + ["B", "Python"]
print(mi_lista)

# eliminar un elemento
mi_lista.pop(-1)
print(mi_lista)

