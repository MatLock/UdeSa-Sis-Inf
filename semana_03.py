import random
from functools import reduce
from random import randrange


def crear_album(figus_total):
    return [0 for _ in range(figus_total)]

def album_incompleto(album):
    return any(elem == 0 for elem in album)

def comprar_figu(figus_total):
    return randrange(figus_total)

def comprar_paquete(figus_total, figus_paquete):
    return [comprar_figu(figus_total) for _ in range(figus_paquete)]

def cuantas_figus(figus_total):
    compras_totales = 0
    album = crear_album(figus_total)
    while album_incompleto(album):
        elem = comprar_figu(figus_total)
        album[elem] = album[elem] + 1
        compras_totales = compras_totales + 1
    return compras_totales

def cuantos_paquetes(figus_total, figus_paquete):
    compras_totales = 0
    album = crear_album(figus_total)
    while album_incompleto(album):
        paquete = comprar_paquete(figus_total, figus_paquete)
        compras_totales += 1
        for i in range(len(paquete)):
            album[paquete[i]] = album[paquete[i]] + 1
    return compras_totales

def experimento_figus(n_repeticiones, figus_total):
    resultados_obtenidos = []
    for i in range(n_repeticiones):
        resultados_obtenidos.append(cuantas_figus(figus_total))
    return reduce(lambda a, b:  a + b, resultados_obtenidos, 0) / n_repeticiones

def experimento_paquete(n_repeticiones, figus_total, figus_paquete):
    resultados_obtenidos = []
    for i in range(n_repeticiones):
        resultados_obtenidos.append(cuantos_paquetes(figus_total, figus_paquete))
    return sum(resultados_obtenidos) / len(resultados_obtenidos)



#if __name__ == '__main__':
    #print(crear_album(5))
    #print(album_incompleto([1,1,1,1]))
    #print(comprar_figu(5))
    #print(cuantas_figus(2))
    #print(experimento_figus(100, 860))
    #print(cuantos_paquetes(12,5))
    #print(experimento_paquete(30,860,5))

