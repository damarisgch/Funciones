#Escriba el teorema de pitágoras que reciba como entrada las longitudes de los dos catetos a y b
# que entregue como salida el largo de la hipotenusa c del triángulo (Ejm a=7,b=5, salida =8,60)

import math
catetoA = int(input('Ingrese el valor del primer cateto:'))
catetoB = int(input('Ingrese el valor del segundo cateto:'))
catetoA = catetoA * catetoA
catetoB = catetoB * catetoB
sumaCatetos = catetoA + catetoB
hipotenusa = math.sqrt(sumaCatetos)
print('Resultado de la hipotenusa es:%f'%(hipotenusa))

