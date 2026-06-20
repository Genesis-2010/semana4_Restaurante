🍽️ Sistema de Gestión de Restaurante
Este es un sistema modular desarrollado en Python que permite gestionar un restaurante administrando sus productos y clientes mediante programación orientada a objetos (POO).

📁 Estructura del Proyecto
Plaintext
Semana4/
└── Restaurante_app/
    ├── modelos/
    │   ├── producto.py
    │   └── usuario.py
    ├── servicios/
    │   └── restaurante.py
    └── main.py
💻 Código Fuente por Módulos
1. Modelos (modelos/)
📦 producto.py
Define la clase para los productos que ofrece el restaurante.

Python
class Producto:
    def __init__(self, nombre, precio, categoria):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria

    def __str__(self):
        return f"Producto: {self.nombre} | Precio: ${self.precio} | Categoría: {self.categoria}"
👤 usuario.py
Define la clase para los clientes o usuarios del sistema.

Python
class Usuario:
    def __init__(self, nombre_usuario, correo):
        self.nombre_usuario = nombre_usuario
        self.correo = correo

    def iniciar_sesion(self):
        return f"El usuario {self.nombre_usuario} ha iniciado sesión."

    def __str__(self):
        return f"Usuario: {self.nombre_usuario} | Correo: {self.correo}"
2. Servicios (servicios/)
🏛️ restaurante.py
Contiene la lógica principal para agrupar, añadir y listar los productos y clientes de un restaurante específico.

Python
class Restaurante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []
        self.clientes = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)

    def mostrar_productos(self):
        print("\n--- PRODUCTOS DISPONIBLES ---")
        for producto in self.productos:
            print(producto)

    def mostrar_clientes(self):
        print("\n--- CLIENTES REGISTRADOS ---")
        for cliente in self.clientes:
            print(cliente)
3. Controlador Principal (main.py)
Une todos los módulos, crea las instancias correspondientes y ejecuta los métodos del restaurante.

Python
# Importación de clases
from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.restaurante import Restaurante

# Crear restaurante
restaurante = Restaurante("Sabor Ecuatoriano")

# Crear productos
producto1 = Producto("Hamburguesa", 5.50, "Comida")
producto2 = Producto("Jugo Natural", 2.00, "Bebida")
producto3 = Producto("Pizza Familiar", 12.00, "Comida")

# Crear clientes
cliente1 = Usuario("María López", "0987654321")
cliente2 = Usuario("Juan Pérez", "0998765432")

# Agregar productos al restaurante
restaurante.agregar_producto(producto1)
restaurante.agregar_producto(producto2)
restaurante.agregar_producto(producto3)

# Agregar clientes al restaurante
restaurante.agregar_cliente(cliente1)
restaurante.agregar_cliente(cliente2)

# Mostrar información registrada
print("=== SISTEMA DE GESTIÓN DE RESTAURANTE ===")
print(f"Restaurante: {restaurante.nombre}")

restaurante.mostrar_productos()
restaurante.mostrar_clientes()
🚀 Cómo Ejecutar el Proyecto
Abre la carpeta principal semana4 en tu terminal de Visual Studio Code.

Ejecuta el archivo principal usando el siguiente comando:

Bash
python Restaurante_app/main.py 