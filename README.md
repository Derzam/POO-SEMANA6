restaurante_app

Sistema de gestión de productos de un restaurante desarrollado en Python aplicando
Programación Orientada a Objetos (herencia, encapsulación y polimorfismo).
Nombre: Derly Zambrano

Descripción

El sistema representa los productos disponibles en un restaurante mediante una
clase padre Producto y dos clases hijas especializadas: Platillo y Bebida.
La clase de servicio Restaurante administra la lista de productos registrados
y permite mostrar su información de forma polimórfica.

Jerarquía de clases

Producto
├── Platillo
└── Bebida

Estructura del proyecto

restaurante_app/
├── modelos/
│   ├── __init__.py
│   ├── producto.py      # Clase padre Producto
│   ├── platillo.py      # Clase hija Platillo
│   └── bebida.py        # Clase hija Bebida
├── servicios/
│   ├── __init__.py
│   └── restaurante.py   # Clase de servicio Restaurante
├── main.py               # Punto de entrada del programa
└── README.md

Detalle de las clases

Producto (modelos/producto.py)

Clase padre con los atributos comunes a todo producto: nombre, precio
(encapsulado como __precio) y disponible.


obtener_precio(): devuelve el precio actual.
cambiar_precio(nuevo_precio): modifica el precio validando que sea mayor que cero
(rechaza valores negativos y también el valor cero).
mostrar_informacion(): método base, sobrescrito por las clases hijas.


Platillo (modelos/platillo.py)

Hereda de Producto mediante super() y agrega:


tipo_platillo: categoría del platillo (entrada, plato fuerte, postre, etc.).
tiempo_preparacion: tiempo estimado de preparación en minutos.


Bebida (modelos/bebida.py)

Hereda de Producto mediante super() y agrega:


volumen_ml: volumen de la bebida en mililitros.
tipo_bebida: tipo de bebida (fría, caliente, alcohólica, etc.).


Restaurante (servicios/restaurante.py)

Clase de servicio que administra una lista de productos:


agregar_producto(producto): agrega un producto a la lista.
mostrar_menu(): recorre la lista y muestra la información de cada producto
llamando a mostrar_informacion() de forma polimórfica.
total_productos(): devuelve la cantidad de productos registrados.


Principios de POO aplicados


Herencia: Platillo y Bebida heredan atributos y comportamiento de Producto.
Encapsulación: el atributo __precio solo puede consultarse o modificarse
mediante obtener_precio() y cambiar_precio(), con validación de valores negativos e iguales a cero.
Polimorfismo: el método mostrar_informacion() se comporta de forma distinta
según el tipo real del objeto (Platillo o Bebida), aunque se invoque desde
la misma lista genérica de productos.


Ejecución

Desde la carpeta raíz del proyecto:

bashpython main.py

