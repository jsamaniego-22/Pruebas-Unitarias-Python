# fabrica_entidades.py
# Ejemplo de patron Factory

from Producto import ProductoDigital, ProductoFisico
from Usuario import Cliente, Administrador

class FabricaEntidades:
    @staticmethod
    def crear_producto(tipo, **kwargs):
        if tipo == 'digital':
            return ProductoDigital(**kwargs)
        elif tipo == 'fisico':
            return ProductoFisico(**kwargs)
        else:
            raise ValueError("Tipo de producto desconocido")

    @staticmethod
    def crear_usuario(tipo, **kwargs):
        if tipo == 'cliente':
            return Cliente(**kwargs)
        elif tipo == 'administrador':
            return Administrador(**kwargs)
        else:
            raise ValueError("Tipo de usuario desconocido")
