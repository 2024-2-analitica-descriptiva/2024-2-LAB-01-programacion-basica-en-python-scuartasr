"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

def lectura_datos(direccion: str, n: int, m: int):

    df = open(direccion, 'r').readlines()
    df = [x.replace('\n', '') for x in df]
    df = [x.split('\t') for x in df]

    #col_n = [x.split(',') for x in col_n]

    # Lista que genera una tupla con cada grupo de letras con el
    # número de línea

    integrador = [(x[n].split(','), x[m]) for x in df]         

    return integrador

def mapper(secuencia: list):
    """
    Esta función recibe una lista de tuplas, donde el primer elemento de cada
    tupla es otra tupla. Se quiere que el elemento de cada tupla se empareje
    con el segundo elemento de la tupla.
    """

    # Lista de separa las letras de cada línea con su respectivo número
    return [(elemento, int(tupla[1])) for tupla in secuencia for elemento in tupla[0]]

def shuffle_and_sort(secuencia: list):
    """
    Esta función recibe una secuencia que es una lista de tuplas, y toma el primer
    elemento de cada una de las tuplas para organizar la lista en función de la
    llave.
    """

    return sorted(secuencia, key=lambda x: x[0])

def reducer(secuencia: list) -> list:
    """
    Esta función recibe una lista de tuplas y la reduce, sumando el valor
    de cada tupla que tienen la misma llave
    """

    retorno = {}

    for tupla in secuencia:
        if tupla[0] in retorno:
            retorno[tupla[0]] += tupla[1]
        else:
            retorno[tupla[0]] = tupla[1]

    return retorno




def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """

    direccion = './files/input/data.csv'

    df = lectura_datos(direccion, 3, 1)

    df = mapper(df)

    df = shuffle_and_sort(df)

    df = reducer(df)

    return df

print(pregunta_11())