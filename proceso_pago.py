# proceso_pago.py

from abc import ABC, abstractmethod

class ProcesoPago(ABC):
    @abstractmethod
    def iniciar_pago(self, monto):
        pass

    @abstractmethod
    def verificar_pago(self):
        pass

    @abstractmethod
    def confirmar_pago(self):
        pass
