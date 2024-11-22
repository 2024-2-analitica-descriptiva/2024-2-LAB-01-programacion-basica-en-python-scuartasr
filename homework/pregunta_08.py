"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

def lectura_datos(direccion, n, m):
    """"
    Esta función lee los datos y los organiza de acuerdo con el interés
    inicial, devolviendo una tupla donde la clave corresponde a la
    n-ésima columna de la base y el valor se asocia co la m-ésima
    columna de la tabla
    """
    
    # Lectura de los datos
    df = open(direccion, 'r').readlines()

    # Separación de los saltos de página
    df = [x.replace('\n', '') for x in df]

    # Creación de una lista por cada instancia de la lista
    df = [x.split('\t') for x in df]

    # Selección de la columna n
    col_n = [int(x[n]) for x in df]

    # Selección de la columna n
    col_m = [x[m] for x in df]

    return list(zip(col_n, col_m))

def shuffle_and_sort(secuencia):
    """
    Ordenada todas las tuplas de la lista de acuerdo con el 
    valor del primer elemento de la lista
    """

    return sorted(secuencia, key=lambda x: x[0])

def reducer(secuencia):
    """
    Recorre todas las tuplas de la lista, agrega los claves que aún
    no estén en un diccionario de referencia, y adjunta los valores
    únicos asociados a esa clase
    """

    # Diccionario de resumen
    resumen = {}

    for tupla in secuencia:
        if tupla[0] in resumen:
            if tupla[1] not in resumen[tupla[0]]:
                resumen[tupla[0]].append(tupla[1])
        else:
            resumen[tupla[0]] = [tupla[1]]

    return [(x, sorted(resumen[x])) for x in resumen]



def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla
    contiene  el valor de la segunda columna; la segunda parte de la tupla
    es una lista con las letras (ordenadas y sin repetir letra) de la
    primera  columna que aparecen asociadas a dicho valor de la segunda
    columna.

    Rta/
    [(0, ['C']),
     (1, ['B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E']),
     (4, ['B', 'E']),
     (5, ['B', 'C', 'D', 'E']),
     (6, ['A', 'B', 'C', 'E']),
     (7, ['A', 'C', 'D', 'E']),
     (8, ['A', 'B', 'D', 'E']),
     (9, ['A', 'B', 'C', 'E'])]

    """

    # Dirección donde se almacenan los datos
    direccion = './files/input/data.csv'

    # Lectura de los datos
    df = lectura_datos(direccion, 1, 0)

    # Ordenamiento de los datos
    df = shuffle_and_sort(df)

    # Creación de las listas de interés
    diccionario = reducer(df)

    return diccionario


