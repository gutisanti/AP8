from tiendalibros.modelo.libro import Libro


class LibroError(Exception):
    def __init__(self, libro: Libro):
        self.libro = libro


class ExistenciasInsuficientesError(LibroError):
    def __init__(self, titulo, isbn, cantidad_a_comprar, existencias):
        super().__init__(f"El libro con título {titulo} y ISBN {isbn} no tiene suficientes existencias para realizar la compra: cantidad a comprar: {cantidad_a_comprar}, existencias: {existencias}")
        self.cantidad_a_comprar = cantidad_a_comprar
        self.existencias = existencias

    def __str__(self):
        return f"El libro con título {self.titulo} y ISBN {self.isbn} no tiene suficientes existencias para realizar la compra: cantidad a comprar: {self.cantidad_a_comprar}, existencias: {self.existencias}"
