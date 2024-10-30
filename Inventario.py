# Inventario.py

class Inventario:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, producto):
        # Usar la propiedad id en lugar de _id
        self.productos[producto.id] = producto

    def obtener_producto_por_id(self, id):
        return self.productos.get(id, None)

    def mostrar_inventario(self):
        for producto in self.productos.values():
            print(producto.mostrar_detalle())

