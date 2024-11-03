# item.py

from abc import ABC, abstractmethod

class Item(ABC):
    def __init__(self, id, nombre, precio):
        self._id = id
        self._nombre = nombre
        self._precio = precio

    # Accesor para ID
    @property
    def id(self):
        return self._id

    # Accesor y mutador para nombre
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        if isinstance(nombre, str) and nombre.strip():
            self._nombre = nombre
        else:
            raise ValueError("Nombre no puede estar vacío")

    # Accesor y mutador para precio
    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, precio):
        if precio >= 0:
            self._precio = precio
        else:
            raise ValueError("Precio no puede ser negativo")

    @abstractmethod
    def mostrar_detalle(self):
        pass
