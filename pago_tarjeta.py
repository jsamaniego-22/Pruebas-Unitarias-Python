# PagoTarjeta.py

from excepciones import PagoFallidoExcepcion

class PagoTarjeta:
    def iniciar_pago(self, monto):
        if monto <= 0:
            raise PagoFallidoExcepcion("El monto del pago debe ser mayor a 0.")
        print(f"Iniciando pago con tarjeta por {monto}...")
        return True

    def verificar_pago(self):
        # Simulación de un fallo
        if not self.simular_respuesta_banco():
            raise PagoFallidoExcepcion("La validación del pago ha fallado.")
        print("Verificando pago con tarjeta...")
        return True

    def confirmar_pago(self):
        print("Pago con tarjeta confirmado.")
        return True
    
    def simular_respuesta_banco(self):
        # Simulación de una respuesta del banco
        return False  # Cambiar a True para simular un éxito
