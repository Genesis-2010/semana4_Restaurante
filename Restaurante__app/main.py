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
