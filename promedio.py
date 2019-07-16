#Calcule el promedio de un curso(Ejm Entrada [70,80,90,100] Salida = 85
suma= 0
for i in range(1,5):
    numero = int(input("Entrada nro.%d:"%(i)))
    suma = suma + numero
promedio = suma/4
print("El promedio es, Salida",promedio)



