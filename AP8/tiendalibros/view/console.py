import sys
from AP8.tiendalibros.modelo.libro_error import LibroError

from tiendalibros.modelo.tienda_libros import TiendaLibros


class UIConsola:

    def __init__(self):
        self.tienda_libros: TiendaLibros = TiendaLibros()
        self.opciones = {
            "1": self.adicionar_un_libro_a_catalogo,
            "2": self.agregar_libro_a_carrito_de_compras,
            "3": self.retirar_libro_de_carrito_de_compras,
            "4": self.salir
        }
    
    def retirar_libro_de_carrito_de_compras(self):
        try:
            isbn = input("Ingrese el ISBN del libro que desea retirar del carrito: ")
            self.tienda_libros.retirar_item_de_carrito(isbn)
            print("Libro retirado del carrito con éxito.")
        except LibroError as e:
            print(f"Error: {e}")

    def agregar_libro_a_carrito_de_compras(self):
        try:
            isbn = input("Ingrese el ISBN del libro que desea agregar al carrito: ")
            cantidad = int(input("Ingrese la cantidad de unidades: "))
            libro = self.tienda_libros.catalogo.get(isbn)

            if libro is None:
                print(f"No existe un libro con ISBN {isbn} en el catálogo.")
                return

            self.tienda_libros.agregar_libro_a_carrito(libro, cantidad)
            print("Libro agregado al carrito con éxito.")
        except ValueError:
            print("Error: La cantidad debe ser un número entero.")
        except LibroError as e:
            print(f"Error: {e}")
    
    def adicionar_un_libro_a_catalogo(self):
        try:
            isbn = input("Ingrese el ISBN del libro: ")
            titulo = input("Ingrese el título del libro: ")
            precio = float(input("Ingrese el precio del libro: "))
            existencias = int(input("Ingrese la cantidad de existencias del libro: "))

            self.tienda_libros.adicionar_libro_a_catalogo(isbn, titulo, precio, existencias)
            print("Libro agregado al catálogo con éxito.")
        except ValueError:
            print("Error: El precio debe ser un número decimal y las existencias deben ser un número entero.")
        except LibroError as e:
            print(f"Error: {e}")

    @staticmethod
    def salir():
        print("\nGRACIAS POR VISITAR NUESTRA TIENDA DE LIBROS. VUELVA PRONTO")
        sys.exit(0)

    @staticmethod
    def mostrar_menu():
        titulo = "¡Tienda Libros!"
        print(f"\n{titulo:_^30}")
        print("1. Adicionar un libro al catálogo")
        print("2. Agregar libro a carrito de compras")
        print("3. Retirar libro de carrito de compras")
        print(f"{'_':_^30}")

    def ejecutar_app(self):
        while True:
            self.mostrar_menu()
            opcion = input("Seleccione una opción: ")
            accion = self.opciones.get(opcion)
            if accion:
                accion()
            else:
                print(f"{opcion} no es una opción válida")

   
