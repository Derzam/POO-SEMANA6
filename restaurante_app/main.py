"""
Punto de entrada del programa.

Crea productos de tipo Platillo y Bebida, los registra en el servicio
Restaurante y muestra el resultado organizado en consola, demostrando
herencia, encapsulación y polimorfismo.
"""

from modelos.platillo import Platillo
from modelos.bebida import Bebida
from servicios.restaurante import Restaurante


def main():
    """Función principal que orquesta la creación y muestra de productos."""

    # Se crea el servicio principal que administrará los productos
    restaurante = Restaurante("Restaurante La Sazon Manaba")

    # ---- Creación de objetos de tipo Platillo (mínimo 3) ----
    entrada = Platillo(
        nombre="Empanadas de carne",
        precio=4.50,
        tipo_platillo="Entrada",
        tiempo_preparacion=10,
    )
    plato_fuerte = Platillo(
        nombre="Bife a la parrilla",
        precio=12.90,
        tipo_platillo="Plato fuerte",
        tiempo_preparacion=25,
    )
    postre = Platillo(
        nombre="Flan casero",
        precio=3.20,
        tipo_platillo="Postre",
        tiempo_preparacion=5,
    )

    # ---- Creación de objetos de tipo Bebida (mínimo 3) ----
    jugo_natural = Bebida(
        nombre="Jugo de naranja natural",
        precio=2.50,
        volumen_ml=300,
        tipo_bebida="Fría",
    )
    cafe = Bebida(
        nombre="Café americano",
        precio=1.80,
        volumen_ml=200,
        tipo_bebida="Caliente",
    )
    cerveza = Bebida(
        nombre="Cerveza artesanal",
        precio=3.75,
        volumen_ml=355,
        tipo_bebida="Alcohólica",
        disponible=False,
    )

    # Se agregan todos los productos al restaurante mediante el servicio
    for producto in (entrada, plato_fuerte, postre, jugo_natural, cafe, cerveza):
        restaurante.agregar_producto(producto)

    # Se muestra el menú completo aplicando polimorfismo
    restaurante.mostrar_menu()

    # ---- Demostración de encapsulación ----
    print("\n--- Demostración de encapsulación en __precio ---")
    print(f"Precio actual de '{cafe.nombre}': ${cafe.obtener_precio():.2f}")
    cafe.cambiar_precio(2.10)
    print(f"Nuevo precio de '{cafe.nombre}': ${cafe.obtener_precio():.2f}")

    # Intentos de asignar precios inválidos (negativo y cero); ambos deben ser rechazados
    cafe.cambiar_precio(-5)
    cafe.cambiar_precio(0)
    print(f"Precio de '{cafe.nombre}' tras los intentos inválidos: ${cafe.obtener_precio():.2f}")

    print(f"\nTotal de productos registrados: {restaurante.total_productos()}")


if __name__ == "__main__":
    main()
