"""
Módulo que define la clase Platillo, hija de Producto.
Representa un platillo o comida preparada del restaurante.
"""

from modelos.producto import Producto


class Platillo(Producto):
    """Clase hija que representa un platillo del restaurante."""

    def __init__(self, nombre, precio, tipo_platillo, tiempo_preparacion, disponible=True):
        """
        Inicializa un platillo reutilizando el constructor de Producto
        mediante super() y agregando los atributos propios de esta clase.

        Args:
            nombre (str): nombre del platillo.
            precio (float): precio del platillo.
            tipo_platillo (str): categoría del platillo (entrada, plato fuerte, postre, etc.).
            tiempo_preparacion (int): tiempo estimado de preparación en minutos.
            disponible (bool): indica si el platillo está disponible actualmente.
        """
        super().__init__(nombre, precio, disponible)  # Reutiliza la lógica del padre
        self.tipo_platillo = tipo_platillo
        self.tiempo_preparacion = tiempo_preparacion

    def mostrar_informacion(self):
        """Sobrescribe el método del padre para mostrar información específica de un platillo."""
        estado = "disponible" if self.disponible else "no disponible"
        print(
            f"Platillo       -> {self.nombre} | Tipo: {self.tipo_platillo} | "
            f"Precio: ${self.obtener_precio():.2f} | "
            f"Preparación: {self.tiempo_preparacion} min | Estado: {estado}"
        )
