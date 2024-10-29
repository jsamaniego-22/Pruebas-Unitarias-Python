# usuario.py

class Usuario:
    def __init__(self, id, nombre, correo_electronico, contrasena):
        self._id = id
        self._nombre = nombre
        self._correo_electronico = correo_electronico
        self._contrasena = contrasena

    @property
    def id(self):
        return self._id

    @property
    def nombre(self):
        return self._nombre

    @property
    def correo_electronico(self):
        return self._correo_electronico

class Cliente(Usuario):
    def __init__(self, id, nombre, correo_electronico, contrasena):
        super().__init__(id, nombre, correo_electronico, contrasena)
        self.historial_compras = []
        self.preferencias = {}

    def agregar_a_historial(self, producto):
        self.historial_compras.append(producto)

class Administrador(Usuario):
    def __init__(self, id, nombre, correo_electronico, contrasena):
        super().__init__(id, nombre, correo_electronico, contrasena)

    def gestionar_inventario(self, inventario, producto, cantidad):
        inventario.actualizar_inventario(producto, cantidad)

