class Producto:
    def __init__(self, nombre, precio, categoria):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria

    def __str__(self):
        return f"Producto: {self.nombre} | Precio: ${self.precio} | Categoría: {self.categoria}"
    

