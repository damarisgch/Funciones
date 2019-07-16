#Invertir un número (Ejm entrada =123,salida = 321)
numero_ingresado = (input("Ingrese un número Entrada: "))
revertir = 0
try:
    valor = int(numero_ingresado)
    while valor > 0:
        residuo = valor % 10
        revertir = (revertir * 10)+ residuo
        valor //=10
        print('Salida: ', revertir)
except ValueError:
    print("Ese número no es valido. Inténtalo de nuevo! ")
