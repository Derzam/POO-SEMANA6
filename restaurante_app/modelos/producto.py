"""
Módulo que define la clase base Producto.
Representa un producto general disponible en el restaurante y concentra
los atributos y comportamientos comunes a todos los productos del menú.
"""


class Producto:
    """Clase padre que representa un producto genérico del restaurante."""

    def __init__(self, nombre, precio, disponible=True):
        """
        Inicializa un producto con sus atributos comunes.

        Args:
            nombre (str): nombre del producto.
            precio (float): precio de venta del producto.
            disponible (bool): indica si el producto está disponible actualmente.
        """
        self.nombre = nombre
        self.__precio = precio  # Atributo encapsulado, protegido de modificaciones directas
        self.disponible = disponible

    def obtener_precio(self):
        """Devuelve el precio actual del producto (método de acceso)."""
        return self.__precio

    def cambiar_precio(self, nuevo_precio):
        """
        Modifica el precio del producto validando que sea mayor que cero
        (método de modificación con validación).

        Args:
            nuevo_precio (float): nuevo valor propuesto para el precio.

        Returns:
            bool: True si el cambio se realizó, False si el valor no era válido.
        """
        if nuevo_precio <= 0:
            print(f"No se pudo actualizar el precio de '{self.nombre}': el precio no puede ser negativo ni igual a cero.")
            return False
        self.__precio = nuevo_precio
        return True

    def mostrar_informacion(self):
        """
        Muestra la información básica del producto.
        Las clases hijas Platillo y Bebida sobrescriben este método
        para mostrar información específica según su tipo (polimorfismo).
        """
        estado = "disponible" if self.disponible else "no disponible"
        print(f"Producto: {self.nombre} | Precio: ${self.__precio:.2f} | Estado: {estado}")
