from Transferencia import Transferencia

class Cuenta ():

    def __init__(self, cajaDeAhorro:str, cantDescubierto:int, retiroMax:int, cantMaxTarjetaCrédito:int, cantMaxChequera:int, maxTransfRecibida:int, comision:float):
        self.cajaDeAhorro = cajaDeAhorro
        self.cantDescubierto = cantDescubierto
        self.retiroMax = retiroMax
        self.cantMaxTarjetaCrédito = cantMaxTarjetaCrédito
        self.cantMaxChequera = cantMaxChequera
        self.maxTransfRecibida = maxTransfRecibida
        self.comision = comision
    
    def __str__(self) -> str:  #Solo para pruebas
        return f"cajaDeAhorro: {self.cajaDeAhorro}, cantDescubierto: {self.cantDescubierto}, retiroMax: {self.retiroMax}, cantMaxTarjetaCrédito: {self.cantMaxTarjetaCrédito}, cantMaxChequera: {self.cantMaxChequera}, maxTransfRecibida: {self.maxTransfRecibida}, comisión: {self.comision}"
    
    def verificarTransferencia(self, transferencia:Transferencia):

        msj = ""

        if transferencia.estado== "ACEPTADA":
            msj = "Transferencia aceptada"

        if transferencia.estado== "RECHAZADA":

            if transferencia.tipo== "RETIRO_EFECTIVO_CAJERO_AUTOMATICO":

                if transferencia.monto > self.retiroMax:
                    msj = "El monto supera el retiro máximo"
                
                elif transferencia.monto > transferencia.saldo + self.cantDescubierto:
                    msj = "El monto supera el saldo y el descubierto"
                
            elif transferencia.tipo == "ALTA_TARJETA_CREDITO":
                if transferencia.targetasActuales >= self.cantMaxTarjetaCrédito:
                    msj = "Se alcanzó el máximo de tarjetas de crédito"
            
            elif transferencia.tipo == "ALTA_CHEQUERA":
                if transferencia.chequerasActuales >= self.cantMaxChequera:
                    msj =  "Se alcanzó el máximo de chequeras"
            
            elif transferencia.tipo == "TRANSFERENCIA_ENVIADA":
                if transferencia.monto*(1+(self.comision/100)) > transferencia.saldo + self.cantDescubierto:
                    msj = "El monto de la transferencia supera el saldo y el descubierto"
            
            elif transferencia.tipo == "TRANSFERENCIA_RECIBIDA" :
                if transferencia.monto > self.maxTransfRecibida and self.maxTransfRecibida != -1:
                    msj = "El monto de la transferencia supera el máximo permitido"
                else:
                    msj =  "Transferencia no autorizada por el banco"

            elif transferencia.tipo == "COMPRAR_DOLAR":
                if "dolar" not in self.cajaDeAhorro:
                    msj =  "El Cliente no tiene caja de ahorro en dolares"    
            
        return f"Fecha: {transferencia.fecha} Tipo: {transferencia.tipo} Estado: {transferencia.estado} Monto: {transferencia.monto} Razon: {msj}"