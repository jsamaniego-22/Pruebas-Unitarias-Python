# interfaz_usuario.py
# Ejemplo de Observadores para la interfaz de usuario y el sistema de inventario

from observer import Observer

class InterfazUsuario(Observer):
    def actualizar(self, mensaje):
        print(f"[InterfazUsuario] Notificación recibida: {mensaje}")
