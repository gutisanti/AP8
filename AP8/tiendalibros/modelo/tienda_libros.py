from AP8.tiendalibros.modelo.carro_compra import CarroCompras
from AP8.tiendalibros.modelo.existencias_insuficientes_error import ExistenciasInsuficientesError
from AP8.tiendalibros.modelo.libro import Libro
from AP8.tiendalibros.modelo.libro_agotado_error import LibroAgotadoError
from AP8.tiendalibros.modelo.libro_error import LibroError
from AP8.tiendalibros.modelo.libro_existente_error import LibroExistenteError


class TiendaLibros:

    def __init__(self):
        self.catalogo = {}
        self.carrito = CarroCompras()

    def adicionar_libro_a_catalogo(self, isbn: str, titulo: str, precio: float, existencias: int):
        if isbn in self.catalogo:
            raise LibroExistenteError(isbn)
        
        nuevo_libro = Libro(isbn, titulo, precio, existencias)
        self.catalogo[isbn] = nuevo_libro
        return nuevo_libro
    
    def agregar_libro_a_carrito(self, libro, cantidad):
        if libro.isbn not in self.catalogo:
            raise LibroError(f"No existe un libro con ISBN {libro.isbn}")

        if libro.existencias == 0:
            raise LibroAgotadoError(libro.titulo, libro.isbn)

        if cantidad > libro.existencias:
            raise ExistenciasInsuficientesError(libro.titulo, libro.isbn, cantidad, libro.existencias)

        self.carrito.agregar_item(libro, cantidad)

    def retirar_item_de_carrito(self, isbn):
        self.carrito.quitar_item(isbn)    
        
    pass
