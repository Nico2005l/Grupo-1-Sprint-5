from Cliente import Cliente
from Cuenta import Cuenta
from Transferencia import Transferencia
import json

# Crear las cuentas

black = Cuenta("peso y dolar", 10000, 500000, 5, 2, -1, 0) #-1 representa que no tiene maximo de transferencias recibidas

gold = Cuenta("dolar", 10000, 20000, 1, 1, 500000, 0.5)

classic = Cuenta("peso", 0, 10000, 0, 0, 150000, 1)

# Abrir y cargar el archivo JSON
with open("mock.json", "r", encoding="utf-8") as json_file:
    json_data = json.load(json_file)


#recorrer el archivo JSON y crear los objetos Cliente y Transferencia

with open("salida.html", "a", encoding="utf-8") as file:
    file.write("<html>")
    file.write("<head>")
    file.write("<title>Reporte de transferencias</title>")
    file.write("</head>")
    file.write("<body>")
    file.write("<h1>Reporte de transferencias</h1>")

for cliente in json_data["usuarios"]:

    if cliente["tipo"] == "black":
        cuenta = black
    elif cliente["tipo"] == "gold":
        cuenta = gold
    else:
        cuenta = classic

    usuario = Cliente(cliente["numero"], cliente["nombre"], cliente["apellido"], cliente["DNI"], cuenta)

    with open("salida.html", "a", encoding="utf-8") as file:
        file.write("<ul>")
        for transferencia in cliente["transacciones"]:
            transaccion = Transferencia(transferencia["tipo"], transferencia["estado"], transferencia["cupoDiarioRestante"], transferencia["monto"], transferencia["saldoEnCuenta"], transferencia["totalTarjetasDeCreditoActualmente"], transferencia["totalChequerasActualmente"], transferencia["fecha"])

            #llamada al metodo que verifica las transferencias
            file.write("<li>"+usuario.verificarTransferencia(transaccion)+"</li>")
        file.write("<br>")
        file.write("</ul>")

with open("salida.html", "a", encoding="utf-8") as file:
    file.write("</body>")
    file.write("</html>")
    
