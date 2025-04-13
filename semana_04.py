import csv
import operator
import itertools

KEYWORD_NOMBRE = 'nombre'
KEYWORD_ESPECIES = 'especies'
KEYWORD_ARBOLES = 'arboles'
KEYWORD_ALTURA = 'altura'
KEYWORD_ORIGEN = 'origen'
KEYWORD_EXOTICO = 'exotico'

NOMBRE_PARQUE = 'espacio_ve'
NOMBRE_ARBOL = 'nombre_com'
NOMBRE_ESPECIE = 'nombre_cie'
ALTURA_ARBOL = 'altura_tot'
ID_ARBOL = 'id_arbol'
RUTA_ARCHIVO = './resources/arbolado-en-espacios-verdes.csv'


def _transformar_archivo_en_arboles(ruta_archivo):
    trees = []
    with open(ruta_archivo, "rt") as fp:
        reader = csv.DictReader(fp)
        for row in reader:
            trees.append({**row})
    return trees


def arboles_parque(ruta_archivo, nombre_parque):
    arboles = _transformar_archivo_en_arboles(ruta_archivo=ruta_archivo)
    arboles_en_parque = [arbol for arbol in arboles if arbol[NOMBRE_PARQUE] == nombre_parque]
    return {arbol[ID_ARBOL]: arbol for arbol in arboles_en_parque}


def arbol_mas_popular(nombre_parque):
    arboles_en_parque = arboles_parque(ruta_archivo=RUTA_ARCHIVO, nombre_parque=nombre_parque)
    aux = {}
    for _, arbol in arboles_en_parque.items():
        if (arbol[NOMBRE_ARBOL] in aux.keys()):
            aux[arbol[NOMBRE_ARBOL]] = aux[arbol[NOMBRE_ARBOL]] + 1
            continue
        aux[arbol[NOMBRE_ARBOL]] = 1
    return max(aux.items(), key=operator.itemgetter(1))[0]


def n_mas_altos(nombre_parque, n_elementos):
    arboles_en_parque = arboles_parque(ruta_archivo=RUTA_ARCHIVO, nombre_parque=nombre_parque)
    aux = [arbol for _, arbol in arboles_en_parque.items()]
    aux.sort(key=lambda arbol: arbol[ALTURA_ARBOL], reverse=True)
    return list(map(lambda arbol: {KEYWORD_NOMBRE: arbol[NOMBRE_ARBOL], KEYWORD_ALTURA: arbol[ALTURA_ARBOL]},
                    aux[:n_elementos]))


def altura_promedio(nombre_parque, especie):
    arboles_en_parque = arboles_parque(ruta_archivo=RUTA_ARCHIVO, nombre_parque=nombre_parque)
    aux = [arbol for _, arbol in arboles_en_parque.items() if arbol[NOMBRE_ESPECIE] == especie]
    return sum(map(lambda arbol: int(arbol[ALTURA_ARBOL]), aux)) / len(aux)


def _arboles_por_parque():
    arboles = _transformar_archivo_en_arboles(ruta_archivo=RUTA_ARCHIVO)
    f_nombre_parque = lambda arbol: arbol[NOMBRE_PARQUE]
    return [{KEYWORD_NOMBRE: k, KEYWORD_ARBOLES: list(v)} for k, v in
            itertools.groupby(sorted(arboles, key=f_nombre_parque), f_nombre_parque)]


def parque_con_mas_arboles(numero_de_parques):
    arboles_por_parque = _arboles_por_parque()
    arboles_por_parque.sort(key=lambda parque: len(parque[KEYWORD_ARBOLES]), reverse=True)
    resultado = []
    for i in range(numero_de_parques):
        resultado.append({arboles_por_parque[i][KEYWORD_NOMBRE]: len(arboles_por_parque[i][KEYWORD_ARBOLES])})
    return resultado


def _promedio_por_parque(arboles_por_parque):
    promedio_por_parque = {}
    for parque in arboles_por_parque:
        total_de_arboles = len(parque[KEYWORD_ARBOLES])
        altura_total = sum([int(arbol[ALTURA_ARBOL]) for arbol in parque[KEYWORD_ARBOLES]])
        promedio_por_parque[parque[KEYWORD_NOMBRE]] = altura_total / total_de_arboles
    return promedio_por_parque


def parques_con_arboles_mas_altos(numero_de_parques):
    arboles_por_parque = _arboles_por_parque()
    promedio_por_parque = _promedio_por_parque(arboles_por_parque)
    total_de_parques = len(promedio_por_parque.keys())
    total_de_promedios = sum([altura_promedio for _, altura_promedio in promedio_por_parque.items()])
    promedio_total = total_de_promedios / total_de_parques
    return [nombre_parque for nombre_parque, promedio in promedio_por_parque.items() if promedio > promedio_total][
           :numero_de_parques]


def _especies_por_parque():
    arboles_por_parque = _arboles_por_parque()
    cantidad_de_especies_por_parque = []
    for parque in arboles_por_parque:
        especies = {}
        for arbol in parque[KEYWORD_ARBOLES]:
            if arbol[NOMBRE_ESPECIE] in especies.keys():
                especies[arbol[NOMBRE_ESPECIE]] = especies[arbol[NOMBRE_ESPECIE]] + 1
                continue
            especies[arbol[NOMBRE_ESPECIE]] = 1
        cantidad_de_especies_por_parque.append({KEYWORD_NOMBRE: parque[KEYWORD_NOMBRE], KEYWORD_ESPECIES: especies})
    return cantidad_de_especies_por_parque


def parque_con_mas_especies(numero_de_parques):
    especies_por_parque = _especies_por_parque()
    especies_por_parque.sort(key=lambda parque: len(parque[KEYWORD_ESPECIES].keys()), reverse=True)
    resultado = []
    for i in range(numero_de_parques):
        resultado.append({KEYWORD_NOMBRE: especies_por_parque[i][KEYWORD_NOMBRE],
                          KEYWORD_ESPECIES: [nombre_especie for nombre_especie in
                                             especies_por_parque[i][KEYWORD_ESPECIES].keys()]})
    return resultado[:numero_de_parques]


def especie_con_mas_ejemplares():
    especies_por_parque = _especies_por_parque()
    contador_especie = {}
    for parque in especies_por_parque:
        for nombre_especie, cantidad in parque[KEYWORD_ESPECIES].items():
            if nombre_especie in contador_especie.keys():
                contador_especie[nombre_especie] = contador_especie[nombre_especie] + cantidad
                continue
            contador_especie[nombre_especie] = cantidad

    especie_con_mayor_cantidad = max(contador_especie, key=contador_especie.get)
    return {especie_con_mayor_cantidad: contador_especie[especie_con_mayor_cantidad]}


def razon_exotico_autoctono():
    arboles = _transformar_archivo_en_arboles(ruta_archivo=RUTA_ARCHIVO)
    exoticos = 0
    autoctonos = 0
    for arbol in arboles:
        if arbol[KEYWORD_ORIGEN] == KEYWORD_EXOTICO:
            exoticos += 1
            continue
        autoctonos += 1
    return exoticos / autoctonos


"""
if __name__ == '__main__':
    print(parque_con_mas_arboles(numero_de_parques=4))
    print(parques_con_arboles_mas_altos(numero_de_parques=4))
    print(parque_con_mas_especies(numero_de_parques=4))
    print(especie_con_mas_ejemplares())
    print(razon_exotico_autoctono())
"""