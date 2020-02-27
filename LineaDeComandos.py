import sys
from conjuntos import  Conjunto

obtenerValores = sys.argv[1:]


"""@andres te toca."""
def SepararConjuntos(texto):
    conjuntos = texto.split("}.{");
    for i in range(len(conjuntos)):
        conjuntos[i] = conjuntos[i].replace("{", "")
        conjuntos[i] = conjuntos[i].replace("}", "")
    return conjuntos

def ProcesarConjuntos(conjuntos):
    listObj = []
    for i in conjuntos:
        elementosDelConjunto = i.split(",")
        listObj.append(Conjunto(elementosDelConjunto,len(elementosDelConjunto)));
    return listObj;

conjuntosSeparados = SepararConjuntos(obtenerValores[0])
conjuntosProcesados = ProcesarConjuntos(conjuntosSeparados)
print(conjuntosSeparados);
print(conjuntosProcesados[0].getUnion(conjuntosProcesados[1]))