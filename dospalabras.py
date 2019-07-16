# Escriba un programa que pida al usuario dos palabras y que indique cuál de ellas es la más larga y por cuántas lo es.

palabra1 = input('Ingresa una palabra:')
palabra2 = input('Ingresa otra palabra:')
conteo1 = len(palabra1)
conteo2 = len(palabra2)
diferencia = abs(conteo1 - conteo2)
if conteo1 > conteo2:
    print('La palabra mayor es:', palabra1)
if conteo1 < conteo2:
    print('La palabra mayor es:', palabra2)
if conteo1 == conteo2:
    print('Las palabras tienen la misma longitud')

    print('La diferencia es de %d letras(s)'% (diferencia))