import sys
from conjuntos import  Conjunto

obtenerValores = sys.argv[1:]

diccionario = {"union":["union","}.{"],"diferencia":["diferencia","}-{"],"interseccion":["interseccion","}/{"]}

operacion = diccionario["union"][0] if diccionario["union"][1] in obtenerValores[0] else \
                diccionario["diferencia"][0] if diccionario["diferencia"][1] in obtenerValores[0] else\
                    diccionario["interseccion"][0] if diccionario["interseccion"][1] in obtenerValores[0] else "null";

print("la operacion es "+ operacion);

"""@andres te toca."""
def SepararConjuntos(texto,operacion):
    conjuntos = texto.split(diccionario.get(operacion)[1]); #interseccion
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

"""def ImprimirConjuntos(conjuntos):
    for i in conjuntos:
        print(i);"""

def RealizarOperacion(conjuntos,operacion):
    return eval("conjuntos[0].get{0}(conjuntos[1])".format(operacion.capitalize()));


if(diccionario.get(operacion)):
    conjuntosSeparados = SepararConjuntos(obtenerValores[0], operacion)
    conjuntosProcesados = ProcesarConjuntos(conjuntosSeparados)
    #ImprimirConjuntos(conjuntosProcesados)
    print(RealizarOperacion(conjuntosProcesados,operacion));
