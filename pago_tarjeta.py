# pago_tarjeta.py

from proceso_pago import ProcesoPago

class PagoTarjeta(ProcesoPago):
    def iniciar_pago(self, monto):
        print(f"Iniciando pago con tarjeta por {monto}...")
        return True

    def verificar_pago(self):
        print("Verificando pago con tarjeta...")
        return True

    def confirmar_pago(self):
        print("Pago con tarjeta confirmado.")
        return True
