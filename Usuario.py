# usuario.py

import re

class Usuario:
    def __init__(self, id, nombre, correo_electronico, contrasena):
        self._id = id
        self._nombre = nombre
        self.correo_electronico = correo_electronico  # Usa el setter para validación
        self._contrasena = contrasena

    @property
    def id(self):
        return self._id

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        if isinstance(nombre, str) and nombre.strip():
            self._nombre = nombre
        else:
            raise ValueError("Nombre no puede estar vacío")

    @property
    def correo_electronico(self):
        return self._correo_electronico

    @correo_electronico.setter
    def correo_electronico(self, correo):
        if re.match(r"[^@]+@[^@]+\.[^@]+", correo):
            self._correo_electronico = correo
        else:
            raise ValueError("Correo electrónico no válido")

    @property
    def contrasena(self):
        return self._contrasena

    @contrasena.setter
    def contrasena(self, contrasena):
        if len(contrasena) >= 6:
            self._contrasena = contrasena
        else:
            raise ValueError("La contraseña debe tener al menos 6 caracteres")


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

