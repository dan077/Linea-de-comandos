import sys

obtenerValores = sys.argv[1:]

#print(obtenerValores);
#modo de escritura.
#{conjunto1}.{conjunto2}
#hol
conjuntos = obtenerValores[0].split("}.{");

print(conjuntos)

for i in conjuntos:
    for j in conjuntos[i]:
    conjuntos[j] = conjuntos[j].replace("{","")
    conjuntos[j] = conjuntos[j].replace("}","")

"""@andres te toca."""
#def separarConjuntos(array):
