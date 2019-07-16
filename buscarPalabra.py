# Se le solicita crear un filtro para buscar palabras en una lista de cadenas.
# Entrada lista = ["vengadores infinity war 2", "VENGADORES: ENDGAME", "X-MEN: FENIX OSCURA", "ALADDIN", "ALADDIN Y LA LAMPARA", "vengadores infinity war"]
# palabra = aladd
# Salida
# res=["ALADDIN", "ALADDIN Y LA LAMPARA"]

numeroPalabras = int(input("Buscar palabras en una lista de cadenas:"))
if numeroPalabras <1:
    print("¡NUL!")
else:
    lista =[]
    for i in range(numeroPalabras):
        print("La palabra es aladd",str(i+1)+ ":",end="")
        palabra = input()
        lista+= [palabra]
        print("La lista buscada es:", lista)

