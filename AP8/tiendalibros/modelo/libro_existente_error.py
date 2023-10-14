from tiendalibros.modelo.libro_error import LibroError


class LibroExistenteError(LibroError):

    def __init__(self, isbn):
        super().__init__(f"El libro con ISBN {isbn} ya existe en el catálogo")

    def __str__(self):
        return f"El libro con título {self.titulo} y ISBN: {self.isbn} ya existe en el catálogo"

   