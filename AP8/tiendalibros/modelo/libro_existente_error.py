from tiendalibros.modelo.libro_error import LibroError


class LibroExistenteError(LibroError):

#class LibroError(Exception):
    pass

#class LibroExistenteError(LibroError):
    def __init__(self, isbn):
        super().__init__(f"El libro con ISBN {isbn} ya existe en el catálogo")

#class Libro:
    def __init__(self, isbn, titulo, precio, existencias):
        self.isbn = isbn
        self.titulo = titulo
        self.precio = precio
        self.existencias = existencias

# Resto de la implementación

#class LibroExistenteError(LibroError):
    def __init__(self, isbn):
        super().__init__(f"El libro con ISBN {isbn} ya existe en el catálogo")

    def __str__(self):
        return f"El libro con título {self.titulo} y ISBN: {self.isbn} ya existe en el catálogo"

    pass
    # Defina metodo inicializador

    # Defina metodo especial
