"""
Módulo que define la clase Bebida, hija de Producto.
Representa una bebida disponible en el restaurante.
"""

from modelos.producto import Producto


class Bebida(Producto):
    """Clase hija que representa una bebida del restaurante."""

    def __init__(self, nombre, precio, volumen_ml, tipo_bebida, disponible=True):
        """
        Inicializa una bebida reutilizando el constructor de Producto
        mediante super() y agregando los atributos propios de esta clase.

        Args:
            nombre (str): nombre de la bebida.
            precio (float): precio de la bebida.
            volumen_ml (int): volumen de la bebida en mililitros.
            tipo_bebida (str): tipo de bebida (fría, caliente, alcohólica, etc.).
            disponible (bool): indica si la bebida está disponible actualmente.
        """
        super().__init__(nombre, precio, disponible)  # Reutiliza la lógica del padre
        self.volumen_ml = volumen_ml
        self.tipo_bebida = tipo_bebida

    def mostrar_informacion(self):
        """Sobrescribe el método del padre para mostrar información específica de una bebida."""
        estado = "disponible" if self.disponible else "no disponible"
        print(
            f"Bebida         -> {self.nombre} | Tipo: {self.tipo_bebida} | "
            f"Precio: ${self.obtener_precio():.2f} | "
            f"Volumen: {self.volumen_ml} ml | Estado: {estado}"
        )
