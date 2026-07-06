"""
Módulo que define la clase de servicio Restaurante.
Administra la lista de productos (platillos y bebidas) del restaurante.
"""


class Restaurante:
    """Clase de servicio encargada de administrar los productos del restaurante."""

    def __init__(self, nombre_restaurante):
        """
        Inicializa el restaurante con una lista vacía de productos.

        Args:
            nombre_restaurante (str): nombre del restaurante.
        """
        self.nombre_restaurante = nombre_restaurante
        self.lista_productos = []

    def agregar_producto(self, producto):
        """
        Agrega un producto (objeto de tipo Platillo o Bebida) a la lista administrada.

        Args:
            producto (Producto): objeto de tipo Producto o alguna de sus clases hijas.
        """
        self.lista_productos.append(producto)
        print(f"Se agregó '{producto.nombre}' al menú de {self.nombre_restaurante}.")

    def mostrar_menu(self):
        """
        Recorre la lista de productos y muestra la información de cada uno.

        Aquí se demuestra el polimorfismo: sin importar si el objeto es un
        Platillo o una Bebida, se llama siempre a mostrar_informacion(), y
        cada clase ejecuta su propia versión sobrescrita del método.
        """
        print(f"\n===== Menú de {self.nombre_restaurante} =====")
        if not self.lista_productos:
            print("Aún no hay productos registrados.")
            return
        for producto in self.lista_productos:
            producto.mostrar_informacion()  # Llamada polimórfica
        print("=" * 45)

    def total_productos(self):
        """Devuelve la cantidad total de productos registrados."""
        return len(self.lista_productos)
