# Se tienen tres diccionarios, se solicita ordenarlos de forma ascendente o descendentes usando el valor de los diccionarios

a={'Jose':18}
b={'Maria':15}
c={'Pedro':24}
a.update(a)
a.update(b)
a.update(c)
w=sorted(a,key=lambda x:a[x],reverse=False)
print(w)
for i in w:
    print("%s:%i"%(i,a[i]))
