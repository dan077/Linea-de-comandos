import sys

obtenerValores = sys.argv[1:]

#print(obtenerValores);
#modo de escritura.
#{conjunto1}.{conjunto2}
#hol
conjuntos = obtenerValores[0].split("}.{");

print(conjuntos)


"""@andres te toca."""
def separarConjuntos(conjuntos):
    for i in range(len(conjuntos)):
        conjuntos[i] = conjuntos[i].replace("{","")
        conjuntos[i] = conjuntos[i].replace("}","")
separarConjuntos()