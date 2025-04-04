

def invertir_lista(lista):
    lista.reverse()
    return lista


def collatz(i):
    if i > 1 and i % 2 == 0:
        return collatz(i / 2) + 1
    if i > 1 and i % 2 != 0:
        return collatz(i * 3 + 1) + 1
    return 0


def contar_definiciones(d):
    temp = {}
    for key, value in d.items():
        temp[key] = len(value)
    return temp


def cantidad_de_claves_letra(d, l):
    temp = 0
    for key in d.keys():
        if key.startswith(l):
            temp += 1
    return temp


def propagacion_a_izquierda(lista, i):
    temp = i
    while temp >= 0 and lista[temp] == 0:
        if lista[temp] == -1:
            return
        lista[temp] = 1
        temp -= 1

def propagacion_a_derecha(lista, i):
    temp = i
    while temp < len(lista) and lista[temp] == 0:
        if lista[temp] == -1:
            return
        lista[temp] = 1
        temp += 1

def propagar(lista):
    for i in range(len(lista)):
        if lista[i] == 1:
            propagacion_a_izquierda(lista, i-1)
            propagacion_a_derecha(lista, i+1)
        if i == len(lista) - 1:
            return lista




#if __name__ == '__main__':
    #print(invertir_lista([1, 2, 3]))
    #print(collatz(7))
    #print(contar_definiciones({"a": ["hola", "hola2","hola3"], "b": ["soy b"]}))
    #print(cantidad_de_claves_letra({"alberto": ["hola"], "pedro": ["pedro"], "anibal": ["fernandez"]}, 'a'))
    #print(propagar([0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0]))
    #print(propagar([0, 0, 0, 1, 0, 0]))
    #print(propagar([0, 0, 0, 0, 0, 1]))
    #print(propagar([0, -1, 0, 0, 0, 1]))
    #print(propagar([0, 1, 0, 0, 0, -1]))



