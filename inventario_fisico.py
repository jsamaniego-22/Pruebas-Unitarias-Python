# inventario_fisico.py

from gestor_inventario import GestorInventario

class InventarioFisico(GestorInventario):
    def __init__(self):
        self.productos = {}

    def añadir_producto(self, producto):
        self.productos[producto.id] = producto
        print(f"Producto físico añadido: {producto.nombre}")

    def eliminar_producto(self, producto_id):
        if producto_id in self.productos:
            del self.productos[producto_id]
            print(f"Producto físico con ID {producto_id} eliminado.")
        else:
            print("Producto no encontrado.")

    def actualizar_stock(self, producto_id, cantidad):
        if producto_id in self.productos:
            self.productos[producto_id].stock += cantidad
            print(f"Stock de producto físico actualizado: {self.productos[producto_id].stock}")
        else:
            print("Producto no encontrado en el inventario físico.")
