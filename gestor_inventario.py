# gestor_inventario.py

from abc import ABC, abstractmethod

class GestorInventario(ABC):
    @abstractmethod
    def añadir_producto(self, producto):
        pass

    @abstractmethod
    def eliminar_producto(self, producto_id):
        pass

    @abstractmethod
    def actualizar_stock(self, producto_id, cantidad):
        pass
