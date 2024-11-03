# observer.py
# Ejemplo de Patron Observe y Notificadot

from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def actualizar(self, mensaje):
        pass
