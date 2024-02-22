"""
EJERCICIO

CREAR UNA CLASE PRODUCTO QUE TENGA 3 HIJOS

ESTA CLASE PRODUCTO VA A TENER
- 3 ATRIBUTOS
- METODO MOSTRAR PRODUCTO QUE DEPENDIENDO EL PRODUCTO
VA A MOSTRAR DIFERENTES CARACTERISTICAS

LIBRO, PELICULA, DISCO - CADA UNA VA A TENER 2 ATRIBUTOS

3 instancias por clase hijo (3 libros, 3 discos y 3 peliculas)
"""

class Producto:

    def __init__(self, precio: float, stock: int, titulo: str):
        self.precio = precio
        self.stock = stock
        self.titulo = titulo

    def mostrar_producto(self):
        pass

class Libro(Producto):

    def __init__(self, precio: float, stock: int, titulo: str, autor: str, cant_paginas: int):
        super().__init__(precio, stock, titulo)
        self.autor = autor
        self.cant_paginas = cant_paginas

    def mostrar_producto(self):
        print(f'-----------------------\n'
              f'Titulo: {self.titulo}\n'
              f'Autor: {self.autor}\n'
              f'Precio: ${self.precio}\n'
              f'Stock: {self.stock}\n'
              f'Cantidad de Páginas: {self.cant_paginas}')

class Disco(Producto):

    def __init__(self, precio: float, stock: int, titulo: str, artista: str, duracion: int):
        super().__init__(precio, stock, titulo)
        self.artista = artista
        self.duracion = duracion

    def mostrar_producto(self):
        print(f'-----------------------\n'
              f'Titulo: {self.titulo}\n'
              f'Artista: {self.artista}\n'
              f'Precio: ${self.precio}\n'
              f'Stock: {self.stock}\n'
              f'Duración: {self.duracion}')

class Pelicula(Producto):

    def __init__(self, precio: float, stock: int, titulo: str, director: str, genero: str):
        super().__init__(precio, stock, titulo)
        self.director = director
        self.genero = genero

    def mostrar_producto(self):
        print(f'-----------------------\n'
              f'Titulo: {self.titulo}\n'
              f'Director: {self.director}\n'
              f'Precio: ${self.precio}\n'
              f'Stock: {self.stock}\n'
              f'Genero: {self.genero}')

libro1 = Libro(precio=5000, autor="Borges", stock=12, titulo="El Aleph", cant_paginas=600)
libro2 = Libro(precio=10000, autor="Edgar Allan Poe", stock=2, titulo="El Cuervo", cant_paginas=200)
libro3 = Libro(precio=25000, autor="Tolkien", stock=20, titulo="El Hobbit", cant_paginas=150)
disco1 = Disco(precio=5000, stock=2, titulo="artaud", artista="Spinetta", duracion=65)
disco2 = Disco(precio=8750, stock=15, titulo="californication", artista="Red Hot CHili Peppers", duracion=74)
disco3 = Disco(precio=1200, stock=1, titulo="Greatest hits", artista="Palito Ortega", duracion=78)
pelicula1 = Pelicula(precio=1000, stock=2, titulo="Buenos Muchachos", director="Scorsese", genero="Drama/Policial")
pelicula2 = Pelicula(precio=4560, stock=0, titulo="Jaws", director="Spielberg", genero="Suspenso")
pelicula3 = Pelicula(precio=2250, stock=16, titulo="Titanic", director="Cameron", genero="Drama/Romantico")

lista_de_productos = [libro1, libro2, libro3, disco1, disco2, disco3, pelicula1, pelicula2, pelicula3]

for producto in lista_de_productos:
    producto.mostrar_producto()