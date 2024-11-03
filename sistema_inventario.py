# sistema_inventario.py
# Ejemplo de Observadores para la interfaz de usuario y el sistema de inventario

from observer import Observer

class SistemaInventario(Observer):
    def actualizar(self, mensaje):
        print(f"[SistemaInventario] Notificación recibida: {mensaje}")
